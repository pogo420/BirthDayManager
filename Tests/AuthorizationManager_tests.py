from Application.AuthorizationManager import AuthorizationManager


def test_create_token():
    """Function for testing token creation check"""
    token = AuthorizationManager().create_token("gupai")
    assert token is not None


def test_token_validate(jwt_details):
    """Function for testing jwt validation"""
    token = AuthorizationManager().create_token(jwt_details.get("data"))
    validation_str = AuthorizationManager().validate_token(jwt_details.get("data"), token)
    assert validation_str.get("data").get("username") == jwt_details.get("data")


def test_token_invalidate(jwt_details):
    """Function for testing jwt invalidation"""
    token = AuthorizationManager().create_token(jwt_details.get("data"))
    validation_str = AuthorizationManager().validate_token(jwt_details.get("data"), "token")
    assert validation_str is None
