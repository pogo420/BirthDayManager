from Application.DbManager import DbManager
from Application.SqLiteHelper import SqLiteHelper


def test_db_connection(env_setup):
    test_string = DbManager(SqLiteHelper, {"db_path": env_setup})\
        .test_connection()
    assert test_string is not None

