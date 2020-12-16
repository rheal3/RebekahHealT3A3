from models.Profile import Profile
from schemas.ProfileSchema import profile_schema, profiles_schema
from main import db
from services.auth_service import verify_user
from sqlalchemy.orm import joinedload
from flask_jwt_extended import jwt_required
from flask import Blueprint, request, jsonify, abort


profiles = Blueprint("profiles", __name__, url_prefix="/profile")


@profiles.route("/", methods=["GET"])
def profile_index():
    profiles = Profile.query.options(joinedload("user")).all()
    return jsonify(profiles_schema.dump(profiles))


@profiles.route("/", methods=["POST"])
@jwt_required
@verify_user
def profile_create(user):

    if user.profile != []:
        return abort(400, description="User already has a profile.")

    profile_fields = profile_schema.load(request.json)
    profile = Profile.query.filter_by(username=profile_fields["username"]).first()

    if profile:
        return abort(400, description="Username already in use.")

    new_profile = Profile()
    new_profile.username = profile_fields["username"]
    new_profile.firstname = profile_fields["firstname"]
    new_profile.lastname = profile_fields["lastname"]
    new_profile.user_id = user.id

    user.profile.append(new_profile)
    db.session.commit()

    return jsonify(profile_schema.dump(new_profile))


@profiles.route("/<int:id>", methods=["GET"])
def profile_show(id):
    profile = Profile.query.get(id)
    return jsonify(profile_schema.dump(profile))


@profiles.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
@verify_user
def profile_update(user, id):

    profile_fields = profile_schema.load(request.json)
    profile = Profile.query.filter_by(id=id, user_id=user.id)
    if not profile:
        return abort(401, description="Unauthorized to update this profile.")

    profile.update(profile_fields)
    db.session.commit()
    return jsonify(profile_schema.dump(profile[0]))


@profiles.route("/<int:id>", methods=["DELETE"])
@jwt_required
@verify_user
def profile_delete(user, id):
    profile = Profile.query.filter_by(id=id, user_id=user.id).first()
    if not profile:
        return abort(400, description="Unauthorized to update this profile.")

        db.session.delete(profile)
        db.session.commit()
        return jsonify(profile_schema.dump(profile))
