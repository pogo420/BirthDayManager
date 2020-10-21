from Application.DbManager import DbManager
from Application.SqLiteHelper import SqLiteHelper


def test_db_connection(env_setup):
    test_string = DbManager(SqLiteHelper, {"db_path": env_setup, "master_table": "birthday_data"})\
        .test_connection()
    assert test_string is not None


def test_db_insert(env_setup, db_insert_test_data, response_test_data):
    test_string = DbManager(SqLiteHelper, {"db_path": env_setup, "master_table": "birthday_data"}) \
        .processor(db_insert_test_data.get("valid"))
    assert test_string == response_test_data.get("valid_insert")

