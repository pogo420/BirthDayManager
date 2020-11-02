"""
Testing config
"""

import os
import pytest

from Application import UserQueryHandler
from Application.UserQueryTranslator import UserQueryTranslator


@pytest.fixture(scope="session")
def env_setup():
    db_path = os.environ["SQLITE_DB"]
    yield db_path


@pytest.fixture(scope="session")
def env_table():
    master_table = os.environ["MASTER_TABLE"]
    yield master_table


@pytest.fixture(scope="session")
def sample_username():
    data = {"username": "ola",
            "password": "ola"}
    yield data


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
def db_read_test_data():
    """function for delete test cases"""
    read_data = {
        "valid": {
            "type": "READ",
            "payload": {
                "name": "gupeh"
            }
        },
        "invalid1": {
            "type": "READ",
            "payload": {
                "name_": "gupeh"
            }
        },
        "invalid2": {
            "type": "READ",
            "payload": {
                "name": "abc"
            }
        }
    }
    yield read_data


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
        },
        "valid_read": {
            "status": "SUCCESS",
            "payload": {
                "message": [('gupeh', '02-10')]
            }
        },
        "invalid_read1": {
            "status": "ERROR",
            "payload": {
                "message": "DATA READ FAILURE"
            }
        },
        "invalid_read2": {
            "status": "SUCCESS",
            "payload": {
                "message": []
            }
        }
    }
    yield response


@pytest.fixture(scope="session")
def client():
    """Important function for flask testing"""
    UserQueryHandler.app.config['TESTING'] = True
    with UserQueryHandler.app.test_client() as client:
        yield client


@pytest.fixture(scope="session")
def jwt_details():
    """Function for all JWT testing"""
    return {
        "data": {
            "hel": 1234},
        "secret": "secret",
        "exp_duration": 10
    }

