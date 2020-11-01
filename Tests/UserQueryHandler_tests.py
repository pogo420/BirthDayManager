

def test_connection(client):
    """Function for testing basic test application"""
    response = client.get("/")
    assert response.data == b'{"message":"Test Response"}\n'



