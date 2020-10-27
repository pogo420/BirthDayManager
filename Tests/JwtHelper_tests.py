import pytest

from Application.JwtHelper import JwtHelper


def test_token_generation(jwt_details):
    """Function for testing jwt token generation"""
    token = JwtHelper() \
        .set_data(jwt_details.get("data"))\
        .set_secret(jwt_details.get("secret"))\
        .set_expiration(jwt_details.get("exp_duration"))\
        .generate_token()
    assert token is not None


def test_token_validate(jwt_details):
    """Function for testing jwt validation"""
    token = JwtHelper() \
        .set_data(jwt_details.get("data")) \
        .set_secret(jwt_details.get("secret")) \
        .set_expiration(jwt_details.get("exp_duration")) \
        .generate_token()

    validation_str = JwtHelper().set_secret(jwt_details.get("secret")).validate_token(token=token)
    assert validation_str.get("data") == jwt_details.get("data")


def test_token_invalidate(jwt_details):
    """Function for testing jwt invalidation"""
    token = JwtHelper() \
        .set_data(jwt_details.get("data")) \
        .set_secret("rubbish") \
        .set_expiration(jwt_details.get("exp_duration")) \
        .generate_token()
    with pytest.raises(Exception) as exp:
        validation_str = JwtHelper().set_secret(jwt_details.get("secret")).validate_token(token=token)
    assert str(exp.value) == "Signature verification failed"

