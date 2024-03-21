"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from api.models import db, Users
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


api = Blueprint('api', __name__)
CORS(api)  # Allow CORS requests to this API


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():
    response_body = {}
    response_body['message'] = "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    return response_body, 200


# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@api.route("/login", methods=["POST"])
def login():
    response_body = {}
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    # Reemplazar por lógica consultando la DB.
    user = db.session.execute(db.select(Users).where(Users.email == email, Users.password == password, Users.is_active == True)).scalar()
    if not user: 
        response_body["message"] = "Email o pasword incorrecto"
        return response_body, 401
    access_token = create_access_token(identity=user.serialize())  # Lo que el back quiere agregar en el token
    response_body['access_token'] = access_token
    response_body['message'] = "Usuario logeado con éxito"
    response_body['results'] = user.serialize()
    return response_body, 200


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@api.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


@api.route('/users/<int:id>', methods=['GET'])
def handle_user_id(id):
    response_body = {} 
    # Buscar usuario por ID
    user = db.session.get(Users,id)
    response_body["results"] = user.serialize()
    response_body["message"] = "Usuario encontrado con éxito."
    return response_body, 200  # Código de estado para "Éxito"

@api.route("/signup", methods=["POST"])
def signup():
    response_body = {}
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    nick_name = request.json.get("nick_name", None)
    user_exists = db.session.execute(db.select(Users).where(Users.email == email)).scalar()
    print(user_exists)
    if user_exists:
        response_body["message"] = "El email ya esta registrado"
        return jsonify(response_body), 400
    new_user = Users(email=email, password=password, is_active=True, nick_name=nick_name, is_admin=False)
    db.session.add(new_user)
    db.session.commit()
    access_token = create_access_token(identity=new_user.serialize()) #preguntar al profe
    response_body["access_token"] = access_token #preguntar al profe
    response_body["message"] = "Usuario registrado con exito"
    response_body["user"] = new_user.serialize()
    return jsonify(response_body), 201

