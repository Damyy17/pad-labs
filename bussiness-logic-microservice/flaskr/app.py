from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}
content = {}
interactions = {}

@app.route('/api/watch', methods=['GET'])
def watch_content():
    user_id = request.args.get('user_id')
    content_id = request.args.get('content_id')
    
    if user_id not in users or content_id not in content:
        return jsonify({"error": "User or content not found"}), 404
    
    interactions[(user_id, content_id)] = "watched"
    
    return jsonify({"message": f"User {user_id} is watching {content_id}"}), 200

@app.route('/api/like', methods=['POST'])
def like_content():
    user_id = request.json.get('user_id')
    content_id = request.json.get('content_id')
    
    if user_id not in users or content_id not in content:
        return jsonify({"error": "User or content not found"}), 404
    
    interactions[(user_id, content_id)] = "liked"
    
    return jsonify({"message": f"User {user_id} liked {content_id}"}), 200

@app.route('/api/history', methods=['GET'])
def get_user_history():
    user_id = request.args.get('user_id')
    
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    user_history = [content_id for (u_id, content_id), interaction in interactions.items() if u_id == user_id]
    
    return jsonify({"user_id": user_id, "history": user_history}), 200

@app.route('/api/rating', methods=['POST'])
def rate_content():
    user_id = request.json.get('user_id')
    content_id = request.json.get('content_id')
    rating = request.json.get('rating')
    
    if user_id not in users or content_id not in content:
        return jsonify({"error": "User or content not found"}), 404
    
    interactions[(user_id, content_id)] = f"rated {rating}"
    
    return jsonify({"message": f"User {user_id} rated {content_id} with {rating} stars"}), 200

@app.route('/api/movies', methods=['POST'])
def add_movie():
    movie_data = request.json
    
    content_id = movie_data.get('content_id')
    content[content_id] = movie_data
    
    return jsonify({"message": f"Movie {content_id} added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)