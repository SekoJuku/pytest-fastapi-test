import os
os.environ["MONGO_URI"] = "mongodb://localhost:27017"
print(os.getenv("MONGO_URI"))
print(dir(os))