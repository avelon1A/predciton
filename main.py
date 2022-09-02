# Import libraries
import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
# Load the model
model = pickle.load(open('model1.pkl', 'rb'))


@app.route('/api', methods=['POST'])
def predict():
    # Get the data from the POST request.
    stock = request.form.get('stock')

    data = request.get_json(force=True)
    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([[159.33500671]])
    # Take the first value of prediction
    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
