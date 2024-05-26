from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Example key store (in a real application, this should be a secure database)
keys = {
    "A16E402B9056E371F36D348AA62BB749": "hyN9IKGfWKdAwFaE5ombSqpu+mo="
}

@app.route('/keys/<key_id>', methods=['GET'])
def get_key(key_id):
    if key_id in keys:
        return jsonify({key_id: keys[key_id]})
    else:
        return jsonify({"error": "Key not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
