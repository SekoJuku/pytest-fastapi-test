from fastapi import FastAPI

from database import Database

def setup():
    DB = Database()
    app = FastAPI()
    DB.insert_one({"name": "test"})
    app.get("/")(lambda: {"message": "Hello World"})
    
    @app.get('/test')
    def test():
        return DB.find_one({'name': 'test'})
    return app

app = setup()