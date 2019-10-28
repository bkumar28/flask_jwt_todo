from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError


regitration_schema = {
                        "type": "object",
                        "properties": {
                            "email_address": {
                                "type": "string",
                                "format": "email"
                            },
                            "password": {
                                "type": "string",
                                "minLength": 7
                            },
                            "firstname": {
                                "type": "string",
                            },
                            "lastname": {
                                "type": "string",
                            }
                        },
                        "required": ["email_address", "password"],
                        "additionalProperties": False
                    }


update_schema = {
                    "type": "object",
                    "properties": {
                        "user_id": {
                        "type": "integer",
                        },
                        "password": {
                            "type": "string",
                            "minLength": 7
                        },
                        "firstname": {
                            "type": "string",
                        },
                        "lastname": {
                            "type": "string",
                        }
                    },
                    "required": ["user_id"],
                    "additionalProperties": False
                }


def validate_registration_form_data(data):
    '''
        Validate User registration form data
        
        @params : data
        @return

    '''

    try:
    
        validate(data, regitration_schema)
    
    except ValidationError as e:
    
        return {'ok': False, 'message': e}
    
    except SchemaError as e:
    
        return {'ok': False, 'message': e}
    
    return {'ok': True, 'data': data}



def validate_user_update_form_data(data):
    '''
        Validate User update form data
        
        @params : data
        @return

    '''

    try:
    
        validate(data, update_schema)
    
    except ValidationError as e:
    
        return {'ok': False, 'message': e}
    
    except SchemaError as e:
    
        return {'ok': False, 'message': e}
    
    return {'ok': True, 'data': data}
