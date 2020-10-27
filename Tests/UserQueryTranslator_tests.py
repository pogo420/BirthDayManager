from Application.UserQueryTranslator import UserQueryTranslator


def test_db_insert(env_setup, db_insert_test_data, response_test_data):
    """Function for DB insert"""
    test_string = UserQueryTranslator(db_insert_test_data.get("valid")).process_data()
    assert test_string == response_test_data.get("valid_insert")


def test_invalid_db_insert(env_setup, db_insert_test_data, response_test_data):
    """Function for DB invalid insert"""
    test_string = UserQueryTranslator(db_insert_test_data.get("invalid")).process_data()
    assert test_string == response_test_data.get("invalid_insert")


def test_db_delete(env_setup, db_delete_test_data, response_test_data):
    """Function for DB delete"""
    test_string = UserQueryTranslator(db_delete_test_data.get("valid")).process_data()
    assert test_string == response_test_data.get("valid_delete")


def test_invalid_db_delete(env_setup, db_delete_test_data, response_test_data):
    """Function for DB invalid delete"""
    test_string = UserQueryTranslator(db_delete_test_data.get("invalid")).process_data()
    assert test_string == response_test_data.get("invalid_delete")


def test_db_read(env_setup, db_insert_test_data, db_read_test_data, response_test_data):
    """Function for testing db read"""
    UserQueryTranslator(db_insert_test_data.get("valid")).process_data()  # inserting data
    test_string = UserQueryTranslator(db_read_test_data.get("valid")).process_data()  # testing
    assert test_string == response_test_data.get("valid_read")


def test_db_invalid_read(env_setup, db_insert_test_data, db_read_test_data, response_test_data):
    """Function for testing invalid db read"""
    UserQueryTranslator(db_insert_test_data.get("valid")).process_data()  # inserting data
    test_string = UserQueryTranslator(db_read_test_data.get("invalid1")).process_data()  # testing
    assert test_string == response_test_data.get("invalid_read1")


def test_db_missing_read(env_setup, db_insert_test_data, db_read_test_data, response_test_data):
    """Function for testing invalid db read"""
    test_string = UserQueryTranslator(db_read_test_data.get("invalid2")).process_data()  # testing
    assert test_string == response_test_data.get("invalid_read2")
