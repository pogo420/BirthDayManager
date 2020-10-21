import os
import pytest


@pytest.fixture(scope="session")
def env_setup():
    db_path = os.environ["SQLITE_DB"]
    yield db_path


@pytest.fixture(scope="session")
def db_insert_test_data():
    insert_data = {
        "valid": {
            "type": "INSERT",
            "payload": {
                "name": "gupei",
                "birthdate": "02-10"
            }
        }
    }
    yield insert_data


@pytest.fixture(scope="session")
def response_test_data():
    response = {
        "valid_insert": {
            "status": "SUCCESS",
            "payload": {
                "message": "DATA INSERT SUCCESS"
            }
        },
        "invalid_insert": {
            "status": "ERROR",
            "payload": {
                "message": "DATA INSERT FAILURE"
            }
        }
    }
    yield response
