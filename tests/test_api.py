def test_login(client):
    response = client.post('/login', json={'username': 'testuser', 'password': 'password'})
    assert response.status_code == 200
    assert 'access_token' in response.json

