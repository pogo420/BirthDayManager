from Application.JwtHelper import JwtHelper
import os


class AuthorizationManager:

    def __init__(self):
        self.auth_helper = JwtHelper
        try:
            self.jwt_secret = os.environ["JWT_SECRET"]
            self.jwt_exp = int(os.environ["JWT_EXPIRE"])
            if self.auth_helper is None:
                raise ValueError("missing jwt secret")
            elif self.jwt_exp is None:
                raise ValueError("missing jwt expiration duration")
        except ValueError as e:
            print(e)

    def create_token(self, username):
        token = JwtHelper() \
            .set_data({"username": username}) \
            .set_secret(self.jwt_secret)\
            .set_expiration(self.jwt_exp)\
            .generate_token()
        return token

    def validate_token(self, username, token):
        try:
            validation_str = JwtHelper().set_secret(self.jwt_secret).validate_token(token=token)
            return validation_str
        except Exception as e:
            print(e)
            return None
