from flask import Flask, request, render_template, jsonify
import pickle

app = Flask(__name__)

# Load vectorizer and model
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("finalized_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    headline = data['headline']
    vect_text = vectorizer.transform([headline])
    prediction = model.predict(vect_text)[0]
    result = "Fake" if prediction == 0 else "Real"  # Adjust as per your model labels
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=True)
