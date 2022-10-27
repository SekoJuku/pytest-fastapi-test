import os
import threading

from pymongo.mongo_client import MongoClient

class Database:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        print("Database init")
        print(os.getenv("MONGO_URI"))
        self._client = MongoClient(os.getenv("MONGO_URI"))
        self.db = self._client['db']
        self.users = self.db["users"]

    def insert_one(self, data):
        return self.users.insert_one(data)

    def find_one(self, data):
        return self.users.find_one(data, {"_id": False})

    def delete_one(self, data):
        return self.users.delete_one(data)

    def delete_all(self):
        return self.users.delete_many({})