"""
Testing script for DbManager class
"""

from Application.DbManager import DbManager
from Application.SqLiteHelper import SqLiteHelper


def test_db_connection(env_setup, env_table):
    """Function for DB testing"""
    test_string = DbManager(SqLiteHelper, {"db_path": env_setup, "master_table": env_table})\
        .test_connection()
    assert test_string is not None


def test_db_insert(env_setup, env_table, db_insert_test_data, response_test_data):
    """Function for DB insert"""
    test_string = DbManager(SqLiteHelper, {"db_path": env_setup, "master_table": env_table}) \
        .processor(db_insert_test_data.get("valid"))
    assert test_string == response_test_data.get("valid_insert")


def test_invalid_db_insert(env_setup, env_table, db_insert_test_data, response_test_data):
    """Function for DB invalid insert"""
    test_string = DbManager(SqLiteHelper, {"db_path": env_setup, "master_table": env_table}) \
        .processor(db_insert_test_data.get("invalid"))
    assert test_string == response_test_data.get("invalid_insert")


def test_db_delete(env_setup, env_table, db_delete_test_data, response_test_data):
    """Function for DB delete"""
    test_string = DbManager(SqLiteHelper, {"db_path": env_setup, "master_table": env_table}) \
        .processor(db_delete_test_data.get("valid"))
    assert test_string == response_test_data.get("valid_delete")


def test_invalid_db_delete(env_setup, env_table, db_delete_test_data, response_test_data):
    """Function for DB invalid delete"""
    test_string = DbManager(SqLiteHelper, {"db_path": env_setup, "master_table": env_table}) \
        .processor(db_delete_test_data.get("invalid"))
    assert test_string == response_test_data.get("invalid_delete")


def test_db_read(env_setup, env_table, db_insert_test_data, db_read_test_data, response_test_data):
    """Function for testing db read"""
    DbManager(SqLiteHelper, {"db_path": env_setup, "master_table": "birthday_data"}) \
        .processor(db_insert_test_data.get("valid"))  # inserting data
    test_string = DbManager(SqLiteHelper, {"db_path": env_setup, "master_table": env_table}) \
        .processor(db_read_test_data.get("valid"))  # testing
    assert test_string == response_test_data.get("valid_read")


def test_db_invalid_read(env_setup, env_table, db_insert_test_data, db_read_test_data, response_test_data):
    """Function for testing invalid db read"""
    DbManager(SqLiteHelper, {"db_path": env_setup, "master_table": "birthday_data"}) \
        .processor(db_insert_test_data.get("valid"))  # inserting data
    test_string = DbManager(SqLiteHelper, {"db_path": env_setup, "master_table": env_table}) \
        .processor(db_read_test_data.get("invalid1"))  # testing
    assert test_string == response_test_data.get("invalid_read1")


def test_db_missing_read(env_setup, env_table, db_insert_test_data, db_read_test_data, response_test_data):
    """Function for testing invalid db read"""
    test_string = DbManager(SqLiteHelper, {"db_path": env_setup, "master_table": env_table}) \
        .processor(db_read_test_data.get("invalid2"))  # testing
    assert test_string == response_test_data.get("invalid_read2")
