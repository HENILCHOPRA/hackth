from flask import Flask, render_template, request
import pickle
app = Flask(__name__)
# Loading the Pre-trained model using Pickle
with open('./LogisticRegression.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def main():
    return jsonify({'message': 'Success',}), 200

if __name__ == '__main__':
    app.run()
