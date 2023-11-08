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
@cache.cached(timeout = 60)
def get_status_cma():
    try:
        response = requests.get(f'{CMA_SERVICE_URL}/status')
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/interactions/view', methods=['POST'])
def create_view_interaction():
    try:
        response = requests.post(f'{CMA_SERVICE_URL}/interactions/view', json=request.json)
        return jsonify(response.json)
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
    

@app.route('/interactions', methods=['GET'])
@cache.cached(timeout = 60)
def get_interactions():
    try:
        response = requests.get(f'{CMA_SERVICE_URL}/interecations')
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# routes for the cr service
@app.route('/cr/status', methods=['GET'])
@cache.cached(timeout = 60)
def get_status_cr():
    try:
        response = requests.get(f'{CR_SERVICE_URL}/status')
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/recommendations/:userId', methods=['GET'])
@cache.cached(timeout = 60)
def get_recommendations():
    try:
        response = requests.get(f'{CR_SERVICE_URL}/recommendations/:userId', json=request.json)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/recommendations/:userId/:contentId', methods=['GET'])
@cache.cached(timeout = 60)
def get_content_from_recommendations():
    try:
        response = requests.get(f'{CR_SERVICE_URL}/recommendations/:userId/:contentId', json=request.json)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500



# routes for creating the content in the cr service
@app.route('/contents', methods=['POST'])
def create_content():
    try:
        response = requests.post(f'{CR_SERVICE_URL}/contents', json=request.json)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/contents', methods=['GET'])
@cache.cached(timeout = 60)
def get_contents():
    try:
        response = requests.get(f'{CR_SERVICE_URL}/contents', json=request.json)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/contents/:contentId', methods=['GET'])
@cache.cached(timeout = 60)
def get_content():
    try:
        response = requests.get(f'{CR_SERVICE_URL}/contents/:contentId', json=request.json)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/contents/:contentId', methods=['PUT'])
def update_content():
    try:
        response = requests.put(f'{CR_SERVICE_URL}/contents/:contentId', json=request.json)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/contents/:contentId', methods=['PUT'])
def delete_content():
    try:
        response = requests.delete(f'{CR_SERVICE_URL}/contents/:contentId', json=request.json)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)