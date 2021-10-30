from flask import Flask, render_template, request, session, redirect, url_for, Response, jsonify, send_from_directory

application = Flask(__name__)

@application.route('/')
def index():
    return jsonify({'message': 'Success',}), 200

@application.route('/register', methods=['POST', 'GET'])
def register():
    if 'user_name' and 'role' in session and session['role'] == 'admin':
        stxid = request.form['contact']
        length = request.form['marital']
        width = request.form['duration']
        height = request.form['age']
        dept = request.form['education']
        dept = request.form['job']
        dept = request.form['month']
        return jsonify({'message': 'Success',}), 200
    else:
        return jsonify({'message': 'Error',}), 500

if __name__ == '__main__':
    application.run(debug=False)
    
