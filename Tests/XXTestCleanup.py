from Application.UserQueryTranslator import UserQueryTranslator


def test_db_cleanup(db_delete_test_data, response_test_data):
    """Function for DB cleanup"""
    test_string = UserQueryTranslator(db_delete_test_data.get("valid")).process_data()
    assert test_string == response_test_data.get("valid_delete")
