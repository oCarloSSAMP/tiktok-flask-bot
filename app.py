from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/spawns')
def spawns():
    try:
        with open("data.json", "r") as f:
            nomes = json.load(f)
        return jsonify({"nomes": nomes})
    except Exception as e:
        return jsonify({"error": str(e), "nomes": []})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
