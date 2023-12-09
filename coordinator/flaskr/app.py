from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Endpoint for coordinating the saga
@app.route('/saga', methods=['POST'])
def saga_orchestrator():
    try:
        data = request.json
        userId = data.get('userId')
        contentId = data.get('contentId')
        comment = data.get('comment')

        # Step 1: Log View Interaction
        interaction_service_url = 'http://gateway:5050/interactions/view'
        response_view = requests.post(interaction_service_url, json={'userId': userId, 'contentId': contentId})
        response_view.raise_for_status()

        # Step 2: Log Comment Interaction
        interaction_service_url = 'http://gateway:5050/interactions/comment'
        response_comment = requests.post(interaction_service_url, json={'userId': userId, 'contentId': contentId, 'comment': comment})
        response_comment.raise_for_status()

        # Step 3: Generate Recommendations
        recommendation_service_url = f'http://gateway:5050/recommendations/{userId}'
        recommendations_response = requests.get(recommendation_service_url)
        recommendations_response.raise_for_status()
        recommendations = recommendations_response.json()

        print('Saga completed successfully')
        return jsonify({'message': 'Saga completed successfully', 'recommendations': recommendations}), 200
    except Exception as e:

        # Compensate for View Interaction
        compensate_view_interaction(userId, contentId)

        # Compensate for Comment Interaction
        compensate_comment_interaction(userId, contentId, comment)

        print(f'Saga failed with error: {str(e)}')
        return jsonify({'message': 'Saga failed with error:','error': str(e)}), 500
    
# Function to compensate for View Interaction
def compensate_view_interaction(userId, contentId):
    interaction_service_url = 'http://gateway:5050/interactions/view/compensate'
    requests.post(interaction_service_url, json={'userId': userId, 'contentId': contentId})
    

# Function to compensate for Comment Interaction
def compensate_comment_interaction(userId, contentId, comment):
    interaction_service_url = 'http://gateway:5050/interactions/comment/compensate'
    requests.post(interaction_service_url, json={'userId': userId, 'contentId': contentId, 'comment': comment})

if __name__ == '__main__':
    app.run(debug=False, port=6060, host="0.0.0.0")
