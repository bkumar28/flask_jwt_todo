from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError

login_schema = {
                "type": "object",
                "properties": {
                    "email_address": {
                        "type": "string",
                        "format": "email"
                    },
                    "password": {
                        "type": "string",
                        "minLength": 7
                    }
                },
                "required": ["email_address", "password"],
                "additionalProperties": False
            }

reset_password_schema = {
                            "type": "object",
                            "properties": {
                                "email_address": {
                                    "type": "string",
                                    "format": "email"
                                },
                                "password": {
                                    "type": "string",
                                    "minLength": 7
                                }
                            },
                            "required": ["email_address"],
                            "additionalProperties": False
                        }

def validate_login_form(data):
    '''
        Validate login form data.

        @params : data
        @return
    '''

    try:
    
        validate(data, login_schema)
    
    except ValidationError as e:
    
        return {'ok': False, 'message': e}
    
    except SchemaError as e:
    
        return {'ok': False, 'message': e}
    
    return {'ok': True, 'data': data}


def validate_reset_password_form(data):
    '''
        Validate reset password form data.

        @params : data
        @return
    '''
    
    try:
    
        validate(data, reset_password_schema)
    
    except ValidationError as e:
    
        return {'ok': False, 'message': e}
    
    except SchemaError as e:
    
        return {'ok': False, 'message': e}
    
    return {'ok': True, 'data': data}


