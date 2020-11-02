"""
Testing script for UserQueryHandler
"""
from json import dumps


def test_connection(client):
    """Function for testing basic test application"""
    response = client.get("/")
    assert response.data == b'Test Response'


def test_authenticate(client, sample_username):
    """Function """
    response = client.get("/authenticate",
                          data=dumps(sample_username),
                          headers={"Content-Type": "application/json"}
                          )
    assert response.data is not None


def test_process_insert(client, sample_username, db_insert_test_data):
    jwt = client.get("/authenticate",
                     data=dumps(sample_username),
                     headers={"Content-Type": "application/json"}
                     )
    response = client.get("/auth/ola/process-data",
                          data=dumps(db_insert_test_data.get("valid")),
                          headers={"Content-Type": "application/json",
                                   "Authorization": "Bearer " + jwt.data.decode("utf-8")}
                          )
    assert response.data.decode("utf-8") == '{"payload":{"message":"DATA INSERT SUCCESS"},"status":"SUCCESS"}\n'


def test_process_read(client, sample_username, db_read_test_data):
    jwt = client.get("/authenticate",
                     data=dumps(sample_username),
                     headers={"Content-Type": "application/json"}
                     )
    response = client.get("/auth/ola/process-data",
                          data=dumps(db_read_test_data.get("valid")),
                          headers={"Content-Type": "application/json",
                                   "Authorization": "Bearer " + jwt.data.decode("utf-8")}
                          )
    assert response.data.decode("utf-8") is not None


def test_process_delete(client, sample_username, db_delete_test_data):
    jwt = client.get("/authenticate",
                     data=dumps(sample_username),
                     headers={"Content-Type": "application/json"}
                     )
    response = client.get("/auth/ola/process-data",
                          data=dumps(db_delete_test_data.get("valid")),
                          headers={"Content-Type": "application/json",
                                   "Authorization": "Bearer " + jwt.data.decode("utf-8")}
                          )
    assert response.data.decode("utf-8") == '{"payload":{"message":"DATA DELETE SUCCESS"},"status":"SUCCESS"}\n'
