from flask_restful import Resource
from flask import request,current_app
from flask_jwt_extended import jwt_required

from app.models.user import User
from app.schemas.user import validate_registration_form_data, validate_user_update_form_data

class Users(Resource):
	'''
		Add
		Update
		Get
		Delete
	'''
	
	@jwt_required
	def get(self):
		'''
			Get user list
	
			@return
		'''
		
		try:
			
			#get user list
			data = User.get_all_users()

			return {"ok":True,'data':data}, 200
		
		except Exception as e:
			
			current_app.logger.error(e)
			return {'ok': False, 'message': 
							"Unexpected error occurred, please try again or contact to administrator !!"}, 403 


	@jwt_required
	def post(self):
		'''
			Add new user by admin

			@return
		'''

		# validate user form data
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
			user.save()
			return {'ok': False, 'message': 'New user added successfully.'}, 201
		
		except Exception as e:
			
			current_app.logger.error(e)
			return {'ok': False, 'message': 
							"Unexpected error occurred, please try again or contact to administrator !!"}, 403 


	@jwt_required
	def put(self):
		'''
			Update existing user data

			@return
		'''

		# validate user form data
		data = validate_user_update_form_data(request.get_json())

		if data['ok'] is False:
			return {'ok': False, 'message': 'Bad request parameters: {}'.format(data['message'])}, 400


		try:

			#update user data
			User.query.filter_by(id=data['data']['user_id']).first().update_user(**data['data'])

		except Exception as e:

			return {'ok': False, 'message': 
						"Unexpected error occurred, please try again or contact to administrator !!"}, 403

		return {'ok': True, 'message': 'User updated successfully!'}, 201




	@jwt_required
	def delete(self):
		'''
			Delete user

			@return
		'''
		
		data = request.get_json()

		if "user_id" not in data:
			return {'ok': False, 'message': 'Bad request parameters: {}'.format(data['message'])}, 403


		try:
			
			# delete user by id
			user_obj = User.delete_user(data['user_id'])
			if user_obj:
				return {'ok': False, 'message': 'user deleted successfully.'}, 201
		
		except Exception as e:
			
			current_app.logger.error(e)
			return {'ok': False, 'message': 
							"Unexpected error occurred, please try again or contact to administrator !!"}, 403 

		return {'ok': False, 'message': 'Invalid user id'}, 400
