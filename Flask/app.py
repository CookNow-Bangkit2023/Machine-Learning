import json
import numpy as np
from flask import Flask, jsonify, request

import filter

app = Flask(__name__)

with open("clean_recipes.json") as f :
    recipes = json.load(f)

@app.route("/recipes", methods=["GET"])
def get_recipes():
    return jsonify(recipes)

@app.route("/predict", methods=["POST"])
def get_predict():
    data = request.get_json(force=True)
    filtered = filter.predict(list(data["ingres"]), recipes)
    prediction = filter.ranking(data["user_id"], filtered)

    return jsonify(prediction)


if __name__ == '__main__':
   app.run(port=5000, debug=True)