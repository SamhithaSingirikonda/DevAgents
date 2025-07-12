'''
Flask backend for login authentication system
Handles user registration and login requests
'''
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
users = {}
@app.route('/register', methods=['POST'])
def register():
    '''Handle user registration with password hashing'''
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'success': False, 'message': 'Username and password required'}), 400
    if username in users:
        return jsonify({'success': False, 'message': 'Username already exists'}), 400
    users[username] = generate_password_hash(password)
    return jsonify({'success': True, 'message': 'User registered successfully'}), 201
@app.route('/login', methods=['POST'])
def login():
    '''Authenticate user credentials'''
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = users.get(username)
    if not user or not check_password_hash(user, password):
        return jsonify({'success': False, 'message': 'Invalid username or password'}), 401
    return jsonify({'success': True, 'message': 'Login successful'}), 200