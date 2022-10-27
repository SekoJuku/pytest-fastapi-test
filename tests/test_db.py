import pytest

from database import Database

DB = Database()

@pytest.mark.hello
def test_ping(mongo_db, client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

@pytest.mark.hello
def test_db(mongo_db, client, user):
    response = client.get("/test")
    assert response.status_code == 200
    print(response.json())
    assert response.json() == {'name': 'test'}
    DB.delete_all()