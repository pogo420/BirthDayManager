from Application.SqLiteHelper import SqLiteHelper
import os
import pytest


def test_connection_test():
    db_path = os.environ["SQLITE_DB"]
    test_string = SqLiteHelper(db_path).create_connection().create_cursor().test_connection()
    assert test_string is not None


def test_insert_data():
    db_path = os.environ["SQLITE_DB"]
    SqLiteHelper(db_path).create_connection().create_cursor().delete_data(
        "name", "'gupeh'", "birthday_data")  # clean up data
    SqLiteHelper(db_path).create_connection().create_cursor().insert_data(
        "name, birthdate", "'gupeh', '02-10'", "birthday_data")  # testing
    test_string = SqLiteHelper(db_path).create_connection().create_cursor().read_data(
        "SELECT * FROM birthday_data where name = 'gupeh'")  # querying data
    assert test_string == [('gupeh', '02-10')]


def test_delete_data():
    db_path = os.environ["SQLITE_DB"]
    SqLiteHelper(db_path).create_connection().create_cursor().delete_data(
        "name", "'gupeh'", "birthday_data")  # clean up data
    SqLiteHelper(db_path).create_connection().create_cursor().insert_data(
        "name, birthdate", "'gupeh', '02-10'", "birthday_data")  # inserting data
    SqLiteHelper(db_path).create_connection().create_cursor().delete_data(
        "name", "'gupeh'", "birthday_data")  # testing
    test_string = SqLiteHelper(db_path).create_connection().create_cursor().read_data(
        "SELECT * FROM birthday_data where name = 'gupeh'")  # querying data
    assert test_string == []


def test_sql_syntax_error():
    db_path = os.environ["SQLITE_DB"]
    with pytest.raises(Exception) as exp:
        SqLiteHelper(db_path).create_connection().create_cursor().read_data(
            "SELECT * FRO birthday_data where name = 'gupeh'")  # querying data
    assert str(exp.value) == """Issue: near "FRO": syntax error"""
