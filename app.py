from flask import Flask, render_template, request, jsonify
import pickle
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)
# Loading the Pre-trained model using Pickle
with open('./my_dumped_classifier (1).pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def main():
    return jsonify({'message': 'Success',}), 200

@app.route('/register', methods=['POST', 'GET'])
def register():
    try:
        params = []
        params.append(int(request.form['contact']))
        params.append(int(request.form['marital']))
        params.append(int(request.form['duration']))
        params.append(int(request.form['age']))
        params.append(int(request.form['education']))
        params.append(int(request.form['job']))
        params.append(int(request.form['month']))
        res = model.predict([params])[0]
        return jsonify({'message': res}), 200
    
    except Exception as e:
        return jsonify({'message': str(e)}), 200

if __name__ == '__main__':
    app.run()
