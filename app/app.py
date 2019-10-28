import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager

from app.conf.logger import LoggerFileHandler

# Initialize Flask Sql Alchemy
db = SQLAlchemy()

def create_app():
    '''
        @return
    '''
    app = Flask(__name__)
    api = Api(app)

    file_handler = LoggerFileHandler.create_logger_file_handler(service_tag="[TODO REST]",
                                                                logger_filename="application.log")

    app.logger.addHandler(file_handler)

    jwt = JWTManager(app)

    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = "\x88\x8fG\xd4\x0c\xaao<\xb7\x99\x0c\xe18\x99\x1bF\x9c+\xd9\x8b\x0b\xa7|\xde"
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://test:test@localhost/test"

    db.init_app(app)


    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        return RevokedToken.is_jti_blacklisted(jti)

    @jwt.unauthorized_loader
    def unauthorized_response(callback):
        return jsonify({
            'ok': False,
            'message': 'Missing Authorization Header'
        }), 401
    
    from app.models.revoked_token import RevokedToken
    from app.auth.routes import Signup, Login, Logout, ResetPassword, TokenRefresh
    from app.user.routes import Users

    api.add_resource(Signup, '/v1/signup')
    api.add_resource(Login, '/v1/login')
    api.add_resource(Logout, '/v1/logout')
    api.add_resource(ResetPassword, '/v1/reset_password')
    api.add_resource(TokenRefresh, '/v1/refresh/token')
    api.add_resource(Users, '/v1/user')

    return app