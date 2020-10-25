

def test_connection(client):
    """Function for testing basic test application"""
    response = client.get("/test")
    assert response.data == b"Test"


def test_valid_read(client):
    """Function for testing valid read"""
    response = client.get("/get/birthday/gupei1/")
    assert response.data == b"UserId:gupei1"

