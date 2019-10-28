from flask_jwt_extended import create_access_token, create_refresh_token
import datetime

class AccessToken(object):
    """
        Generate Access token by email address and will expire after 24 hours

    """

    @staticmethod
    def get_user_token(email_address):
        '''
            Generate access and refresh token.

            @parmas : email_address
            @return
        '''
        expires = datetime.timedelta(days=1)
        token = {}
        token['access_token'] = create_access_token(identity=email_address, expires_delta=expires)
        token['refresh_token'] = RefeshToken().get_refresh_token(email_address,expires)
        return token


class RefeshToken(object):
    """
        Generate referesh token
    """

    @staticmethod
    def get_refresh_token(email_address, expires=None):
        '''
            Generate refresh token.

            @params : email_address
            @params : expires
            @return
        '''
        
        if expires:
            expires = datetime.timedelta(days=1)

        return create_refresh_token(identity=email_address, expires_delta=expires)
