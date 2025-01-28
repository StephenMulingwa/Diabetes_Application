from flask import Flask, render_template, request
import pickle

with open('../Diabetes_Prediction.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return 'Hello World'

@app.route('/predict', methods=['GET','POST'])
def predict():
    user_input = request.form['text']


if __name__ == '__main__':
    app.run(debug=True)