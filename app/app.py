from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load a dummy model (replace with your own model)
try:
    with open("app/model.pkl", "rb") as f:
        model = pickle.load(f)
except:
    model = None  # Placeholder

@app.route("/")
def index():
    return "ML-Magic-API is running ✨"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = np.array(data.get("features")).reshape(1, -1)

    if model:
        prediction = model.predict(features)[0]
        return jsonify({"result": str(prediction)})
    else:
        return jsonify({"error": "Model not found"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
