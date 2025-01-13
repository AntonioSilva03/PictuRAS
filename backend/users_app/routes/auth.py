from flask import Blueprint, jsonify, request # type: ignore
from flask_jwt_extended import create_access_token # type: ignore
from werkzeug.security import check_password_hash # type: ignore
from controllers.user import *
from models.user import User
import traceback

auth__blueprint = Blueprint('auth', __name__)


@auth__blueprint.route('/register', methods=['POST'])
def register():
    try:
        user = insert_user(User(**request.json))
        access_token = create_access_token(identity=user.username)
        return jsonify(user.to_json(), access_token=access_token), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': f'{e}'}), 400


@auth__blueprint.route('/login', methods=['POST'])
def login():
    try:
        username = request.json['username']
        password= request.json['password']
        user = find_by_username(username)

        if not check_password_hash(user.password, password):
            raise Exception('Invalid username or password')

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': f'{e}'}), 401