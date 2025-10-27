from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for your static site

# Get your secret API URL from environment variable
SECRET_API_URL = os.environ.get('SECRET_API_URL')

@app.route('/api/download', methods=['POST'])
def download_proxy():
    try:
        # Get the request data from frontend
        data = request.json
        
        # Forward the request to your actual API
        response = requests.post(
            SECRET_API_URL,
            json=data,
            timeout=30
        )
        
        # Return the response back to frontend
        return jsonify(response.json()), response.status_code
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  
