from models.User import User
from schemas.UserSchema import user_schema
from main import db, bcrypt
from flask_jwt_extended import create_access_token
from datetime import timedelta
from flask import Blueprint, request, jsonify, abort

auth = Blueprint('auth', __name__, url_prefix="/auth")


@auth.route("/register", methods=["POST"])
def auth_register():
    """
    Creates a new user in the app

    Returns:
    Dict of new user
    """

    user_fields = user_schema.load(request.json)

    # Check if user email already in use, return abort instead of getting errors
    if User.query.filter_by(email=user_fields["email"]).first():
        return abort(400, description="Email already registered.")

    user = User()
    user.email = user_fields["email"]
    user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")
    user.admin = user_fields["admin"]

    db.session.add(user)
    db.session.commit()

    return jsonify(user_schema.dump(user))


@auth.route("/login", methods=["POST"])
def auth_login():
    """
    Logs user in using email/password and returns JWT for authorization to use other endpoints

    Returns:
    Dict containing JWT for user
    """
    user_fields = user_schema.load(request.json)

    user = User.query.filter_by(email=user_fields["email"]).first()

    if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return abort(401, description="Invalid login details.")

    expiry = timedelta(days=1)
    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)

    return jsonify({"token": access_token})
