from flask import Flask, render_template, request, jsonify
import pickle
import json
from sklearn.linear_model import LogisticRegression
from flask_cors import CORS,cross_origin

app = Flask(__name__)
CORS(app)

# Loading the Pre-trained model using Pickle
with open('./my_dumped_classifier (1).pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def main():
    return jsonify({'message': 'Success',}), 200

@app.route('/register', methods=['POST', 'GET'])
@cross_origin()
def register():
    dic = {'contact': {0: 'cellular', 1: 'telephone', 2: 'unknown'},
         'education': {0: 'primary', 1: 'secondary', 2: 'tertiary', 3: 'unknown'},
         'job': {0: 'admin.',
          1: 'blue-collar',
          2: 'entrepreneur',
          3: 'housemaid',
          4: 'management',
          5: 'retired',
          6: 'self-employed',
          7: 'services',
          8: 'student',
          9: 'technician',
          10: 'unemployed',
          11: 'unknown'},
         'marital': {0: 'divorced', 1: 'married', 2: 'single'},
         'month': {0: 'apr',
          1: 'aug',
          2: 'dec',
          3: 'feb',
          4: 'jan',
          5: 'jul',
          6: 'jun',
          7: 'mar',
          8: 'may',
          9: 'nov',
          10: 'oct',
          11: 'sep'}}
    try:
        values = []
        try:
            temp = request.args.get('contact').lower()
            val = list(dic['contact'].keys())[list(dic['contact'].values()).index(temp)]
            values.append(val)
        except:
            values.append(2)
        try:
            temp = request.args.get('marital').lower()
            val = list(dic['marital'].keys())[list(dic['marital'].values()).index(temp)]
            values.append(val)
        except:
            values.append(2)

        values.append(int(request.args.get('duration')))
        values.append(int(request.args.get('age')))
        try:
            temp = request.args.get('education').lower()
            val = list(dic['education'].keys())[list(dic['education'].values()).index(temp)]
            values.append(val)
        except:
            values.append(3)

        try:
            temp = request.args.get('job').lower()
            val = list(dic['job'].keys())[list(dic['job'].values()).index(temp)]
            values.append(val)
        except:
            values.append(11)
        try:
            temp = request.args.get('month').lower()
            val = list(dic['month'].keys())[list(dic['month'].values()).index(temp)]
            values.append(val)
        except:
            values.append(1)
        print(values)
        res = model.predict([values])
        return jsonify({'message': str(res[0])}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 200

if __name__ == '__main__':
    app.run(debug = True)
