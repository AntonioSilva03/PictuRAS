from flask import Blueprint, jsonify, request # type: ignore
from flask_jwt_extended import create_access_token # type: ignore
from models.user import User
from werkzeug.security import check_password_hash # type: ignore

users__blueprint = Blueprint('user', __name__)
