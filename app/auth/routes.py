from flask_restful import Resource
from flask import request,current_app
from flask_jwt_extended import jwt_required, get_jwt_identity, jwt_refresh_token_required,get_raw_jwt

from app.models.user import User
from app.models.revoked_token import RevokedToken

from app.utils.jwt_token import AccessToken,RefeshToken

from app.schemas.login import validate_login_form,validate_reset_password_form
from app.schemas.user import validate_registration_form_data


class Signup(Resource):

	'''
		Register new user
	'''

	def post(self):
		'''
			1. Validate user registration form data
			2. Validate user email address is already exist or not
			3. Register new user
			4. Return user_id with access token and refresh token.

			@return
		'''

		# validate user registration form data
		data = validate_registration_form_data(request.get_json())
		
		if data['ok'] is False:
		
			return {'ok': False, 'message': 'Bad request parameters: {}'.format(data['message'])}, 400

		# initialize user instance 
		user = User(data['data'])

		# validate user email address is already exist or not
		if user.find_by_email_address(data['data']['email_address']):
		
			return {'ok': False, 'message': 'This email address already exist: {}, '
											'Please try other email address'.format(data['data']['email_address'])}, 400
		try:
			
			# save new user registration form data.
			user = user.save()

			if user:
		
				# generate access and refresh token by email address
				res = AccessToken.get_user_token(data['data']['email_address'])
				res['user_id'] = user.id
				res['ok'] = True
				return res, 201
		
		except Exception as e:
			current_app.logger.error(e)
		
		return {'ok': False, 'message': 
				"Unexpected error occurred, please try again or contact to administrator !!"}, 403 


class Login(Resource):
	'''
		Register user login
	'''

	def post(self):

		'''
			1. Validate login form data.
			2. Find user by email address.
			3. Validate user login password
			4. Return user_id with access token and refresh token.

			@return
		'''

		# validate login form data
		data = validate_login_form(request.get_json())
		
		if data['ok'] is False:
		
			return {'ok': False, 'message': 'Bad request parameters: {}'.format(data['message'])}, 400

		try:

			# find user by email address
			user = User.query.filter_by(email_address=data['data']['email_address']).first()
		
		except Exception as e:

			current_app.logger.error(e)
			return {'ok': False, 'message': 
							"Unexpected error occurred, please try again or contact to administrator !!"}, 403

		if not user:
		
			return {'ok': False,'message': 'Email address {} doesn\'t exist'.format(data['data']['email_address'])},400

		# validate user login password
		if user.verify_hash(data['data']['password'], user.password):
		
			# generate access and refresh token by email address
			res = AccessToken.get_user_token(data['data']['email_address'])
			res['user_id'] = user.id
			res['ok'] = True
			return res, 201
		
		else:
		
			return {'ok': False,'message': 'Invalid credentials'},403


class Logout(Resource):
	'''
		Logout user
	'''

	@jwt_required
	def post(self):

		'''
			save user access token into blacklist, so no more will be access
			protected resource by current access token

		'''

		# Get user jti payload
		jti = get_raw_jwt()['jti']
		
		try:
			# Revoke user access token and save into blacklist, so no more will 
			# be access portected resource by current access token.
			revoked_token = RevokedToken(jti = jti,user_identity=get_jwt_identity())
			revoked_token.save()

			return {'ok': True,'message': 'Access token has been revoked'},201
		
		except Exception as ese:
			
			current_app.logger.info(ese)

			return {'ok': False, 'message': 
							"Unexpected error occurred, please try again or contact to administrator !!"}, 403 


class ResetPassword(Resource):
	'''
		Reset user password.
	'''

	def post(self):

		'''
			1. Validate reset password form data
			2. Find user by email address.
			3. Update user password

			@return
		'''

		# validate reset password form data
		data = validate_reset_password_form(request.get_json())
		
		if data['ok'] is False:
		
			return {'ok': False, 'message': 'Bad request parameters: {}'.format(data['message'])}, 400

		try:
			
			# find user by email address
			user = User.query.filter_by(email_address=data['data']['email_address']).first()

		except Exception as e:

			current_app.logger.error(e)
			return {'ok': False, 'message': 
							"Unexpected error occurred, please try again or contact to administrator !!"}, 403 

		if not user:
		
			return {'ok': False, 'message': 'Email address {} doesn\'t exist'.format(data['data']['email_address'])},400

		try:
			
			# update user password
			user.update_user(**{'password':data['data']['password']})

		except Exception as e:

			current_app.logger.error(e)
			return {'ok': False, 'message': 
							"Unexpected error occurred, please try again or contact to administrator !!"}, 403 

		return {"ok":True,"message":"Password reset successfully"},201


class TokenRefresh(Resource):
	'''
		Generate access and refresh token
	'''

	@jwt_refresh_token_required
	def post(self):
		'''
			Generate register user access and refresh token

			@return
		'''
		jti = get_jwt_identity()
		data = AccessToken.get_user_token(jti)
		data['ok'] = True

		return data,201
