import os

import pytest
from fastapi.testclient import TestClient
from testcontainers.mongodb import MongoDbContainer


@pytest.fixture(scope="session")
def mongo_db():
    with MongoDbContainer("mongo:6.0.2-focal") as mongo:
        update_url(mongo)
        print(os.getenv("MONGO_URI"))
        yield mongo

def update_url(mongo):
    os.environ["MONGO_URI"] = "mongodb://{username}:{password}@{host}:{port}".format(
        username=mongo.MONGO_INITDB_ROOT_USERNAME,
        password=mongo.MONGO_INITDB_ROOT_PASSWORD,
        host="localhost",
        port=mongo.get_exposed_port(27017),
    )

@pytest.fixture(scope="session")
def DB(mongo_db, client):
    from database import Database
    
    DB = Database()
    return DB

@pytest.fixture(scope="session")
def client(mongo_db):
    from app.main import setup
    app = setup()
    return TestClient(app)

@pytest.fixture(scope="session")
def user(DB):
    test_user = create_user()
    DB.insert_one(test_user)
    return DB.find_one(test_user)

def create_user():
    return {"name": "user_test"}