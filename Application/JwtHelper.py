import jwt
import datetime


class JwtHelper:
    """Helper class for JWT features"""

    def __init__(self):
        self.expiration_duration = None
        self.data = None
        self.secret = None

    def set_expiration(self, expiration_duration: int) -> 'JwtHelper':
        self.expiration_duration = datetime.datetime.utcnow()\
                                   + datetime.timedelta(seconds=expiration_duration)
        return self

    def set_data(self, data: dict) -> 'JwtHelper':
        self.data = data
        return self

    def set_secret(self, secret: str) -> 'JwtHelper':
        self.secret = secret
        return self

    def generate_token(self) -> bytes:
        payload = {
            "data": self.data,
            "exp": self.expiration_duration
        }
        token = jwt.encode(payload=payload, key=self.secret, algorithm="HS256")
        return token

    def validate_token(self, token: bytes):
        return jwt.decode(jwt=token, key=self.secret, algorithms="HS256")

