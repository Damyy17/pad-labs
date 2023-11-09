from flask import Flask, jsonify, request, redirect
from flask_caching import Cache
import requests

app = Flask(__name__)
# initializing Flask Cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})


# Configuration for microservice endpoints
CMA_SERVICE_URL = "http://localhost:3000" 
CR_SERVICE_URL = "http://localhost:4000" 

# routes for the cma service
@app.route('/cma/status', methods=['GET'])
def get_status_cma():
    try:
        response = requests.get(f'{CMA_SERVICE_URL}/cma/status')
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/interactions/view', methods=['POST'])
def log_view_interaction():
    interaction_data = request.get_json()
    response = requests.post(f"{CMA_SERVICE_URL}/interactions/view", json=interaction_data)
    return response.json(), response.status_code


@app.route('/interactions/like', methods=['POST'])
def log_like_interaction():
    interaction_data = request.get_json()
    response = requests.post(f"{CMA_SERVICE_URL}/interactions/like", json=interaction_data)
    return response.json(), response.status_code


@app.route('/interactions/comment', methods=['POST'])
def log_comment_interaction():
    interaction_data = request.get_json()
    response = requests.post(f"{CMA_SERVICE_URL}/interactions/comment", json=interaction_data)
    return response.json(), response.status_code


@app.route('/interactions/add-to-favorites', methods=['POST'])
def log_add_to_favorites_interaction():
    interaction_data = request.get_json()
    response = requests.post(f"{CMA_SERVICE_URL}/interactions/add-to-favorites", json=interaction_data)
    return response.json(), response.status_code


@app.route('/interactions', methods=['GET'])
@cache.cached(timeout = 60)
def get_all_interactions():
    response = requests.get(f"{CMA_SERVICE_URL}/interactions")
    return response.json(), response.status_code


# routes for the cr service
@app.route('/cr/status', methods=['GET'])
def get_status_cr():
    try:
        response = requests.get(f'{CR_SERVICE_URL}/cr/status')
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/recommendations/<userId>', methods=['GET'])
@cache.cached(timeout = 60)
def get_recommendations(userId):
    response = requests.get(f"{CR_SERVICE_URL}/recommendations/{userId}")
    return response.json(), response.status_code
    

@app.route('/recommendations/<userId>/<contentId>', methods=['GET'])
@cache.cached(timeout = 60)
def get_content_from_recommendations(userId, contentId):
    response = requests.get(f"{CR_SERVICE_URL}/recommendations/{userId}/{contentId}")
    return response.json(), response.status_code


# routes for creating the content in the cr service
@app.route('/contents', methods=['POST'])
def create_content():
    content_data = request.get_json()
    response = requests.post(f"{CR_SERVICE_URL}/contents", json=content_data)
    return response.json(), response.status_code


@app.route('/contents', methods=['GET'])
@cache.cached(timeout = 60)
def get_all_contents():
    response = requests.get(f"{CR_SERVICE_URL}/contents")
    return response.json(), response.status_code


@app.route('/contents/<contentId>', methods=['GET'])
@cache.cached(timeout = 60)
def get_content(contentId):
    response = requests.get(f"{CR_SERVICE_URL}/contents/{contentId}")
    return response.json(), response.status_code


@app.route('/contents/<contentId>', methods=['PUT'])
def update_content(contentId):
    content_data = request.get_json()
    response = requests.put(f"{CR_SERVICE_URL}/contents/{contentId}", json=content_data)
    return response.json(), response.status_code


@app.route('/contents/<contentId>', methods=['DELETE'])
def delete_content(contentId):
    response = requests.delete(f"{CR_SERVICE_URL}/contents/{contentId}")
    return response.json(), response.status_code


if __name__ == '__main__':
    app.run(debug=True, port=5050)