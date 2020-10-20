from Application.SqLiteHelper import SqLiteHelper
import os
from Application.StatusCodes import StatusCodes
import pytest


@pytest.fixture(scope="session")
def env_setup():
    db_path = os.environ["SQLITE_DB"]
    yield db_path


def test_connection_test(env_setup):
    db_path = env_setup
    test_string = SqLiteHelper(db_path).create_connection().create_cursor().test_connection()
    assert test_string is not None


def test_insert_data(env_setup):
    db_path = env_setup
    SqLiteHelper(db_path).create_connection().create_cursor().delete_data(
        "name", "'gupeh'", "birthday_data")  # clean up data
    SqLiteHelper(db_path).create_connection().create_cursor().insert_data(
        "name, birthdate", "'gupeh', '02-10'", "birthday_data")  # testing
    test_string = SqLiteHelper(db_path).create_connection().create_cursor().read_data(
        "SELECT * FROM birthday_data where name = 'gupeh'")  # querying data
    assert test_string == [('gupeh', '02-10')]


def test_delete_data(env_setup):
    db_path = env_setup
    SqLiteHelper(db_path).create_connection().create_cursor().delete_data(
        "name", "'gupeh'", "birthday_data")  # clean up data
    SqLiteHelper(db_path).create_connection().create_cursor().insert_data(
        "name, birthdate", "'gupeh', '02-10'", "birthday_data")  # inserting data
    SqLiteHelper(db_path).create_connection().create_cursor().delete_data(
        "name", "'gupeh'", "birthday_data")  # testing
    test_string = SqLiteHelper(db_path).create_connection().create_cursor().read_data(
        "SELECT * FROM birthday_data where name = 'gupeh'")  # querying data
    assert test_string == []


def test_sql_syntax_error_read(env_setup):
    db_path = env_setup
    test_string = SqLiteHelper(db_path).create_connection().create_cursor().read_data(
            "SELECT * FRO birthday_data where name = 'gupeh'")  # querying data
    assert test_string == StatusCodes.DATA_READ_FAILURE
