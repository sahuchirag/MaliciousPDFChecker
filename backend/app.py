from flask import Flask, request, render_template
import pickle
from feature_extraction import feature_extraction

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def helloWorld():
    return "<p>Hello World!</p>"

@app.route('/result', methods=['GET','POST'])
def result():
    form = request.form

    # run test code here
    # import classifier module
    extracted_features = feature_extraction()
    prediction = model.predict(extracted_features)
    # if request.method == 'POST':

    # output = request.get_json()
    return {"malicious": "Yes"}

if __name__ == '__main__':
    # run training model here
    app.run(debug=True, port=2000)