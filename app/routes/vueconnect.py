from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/api/data/")
def get_data():
    return jsonify({"message": "Hello it's flask API"}), 200

@app.post("/api/data/")
def post_data():
    data = request.json
    return jsonify({"received data": data}), 200

if __name__ == "__main__":
    app.run(port=10000, debug=True)