from flask import Flask, jsonify, request, redirect
import requests

app = Flask(__name__)

# Configuration for microservice endpoints
CMA_SERVICE_URL = "http://localhost:3000" 
CR_SERVICE_URL = "http://localhost:4000" 

# routes for the cma service
@app.route('/interactions/view', methods=['POST'])
def create_view_interaction():
    try:
        response = requests.post(f'{CMA_SERVICE_URL}/interactions/view', json=request.json)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/interactions/like', methods=['POST'])
def create_like_interaction():
    try:
        response = requests.post(f'{CMA_SERVICE_URL}/interactions/like', json=request.json)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/interactions/comment', methods=['POST'])
def create_comment_interaction():
    try:
        response = requests.post(f'{CMA_SERVICE_URL}/interactions/comment', json=request.json)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/interactions/add-to-favorites', methods=['POST'])
def create_add_to_favorites_interaction():
    try:
        response = requests.post(f'{CMA_SERVICE_URL}/interactions/add-to-favorites', json=request.json)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/interactions/status', methods=['GET'])
def get_status():
    try:
        response = requests.get(f'{CMA_SERVICE_URL}/status')
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)