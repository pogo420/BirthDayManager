import os
import pytest


@pytest.fixture(scope="session")
def env_setup():
    db_path = os.environ["SQLITE_DB"]
    yield db_path


@pytest.fixture(scope="session")
def db_insert_test_data():
    """Function for insert data"""
    insert_data = {
        "valid": {
            "type": "INSERT",
            "payload": {
                "name": "gupeh",
                "birthdate": "02-10"
            }
        },
        "invalid": {
            "type": "INSERT",
            "payload": {
                "name_": "gupeh",
                "birthdate": "02-10"
            }
        }
    }
    yield insert_data


@pytest.fixture(scope="session")
def db_delete_test_data():
    """function for delete test cases"""
    insert_data = {
        "valid": {
            "type": "DELETE",
            "payload": {
                "name": "gupeh"
            }
        },
        "invalid": {
            "type": "DELETE",
            "payload": {
                "name_": "gupeh"
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
        },
        "valid_delete": {
            "status": "SUCCESS",
            "payload": {
                "message": "DATA DELETE SUCCESS"
            }
        },
        "invalid_delete": {
            "status": "ERROR",
            "payload": {
                "message": "DATA DELETE FAILURE"
            }
        }
    }
    yield response
