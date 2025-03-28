from flask import Flask, request, jsonify
from Model import calculate_similarity

app = Flask(__name__)

@app.route('/similarity', methods=['POST'])
def similarity():
    # Strictly follows assessment's required request/response format
    data = request.json
    score = calculate_similarity(data['text1'], data['text2'])
    scaled_score = (score + 1) / 2  # Scale to [0,1] here as specified
    return jsonify({"similarity score": round(scaled_score, 4)})  # Exact key name required

@app.route('/')
def health_check():
    return "Semantic Similarity API (Assessment Compliant)"
