from bson import ObjectId
from database.mongodb_connection import get_mongo_client

class LogRepository:
    def __init__(self):
        self.client = get_mongo_client()
        self.db = self.client["your_database_name"] #gak sengaja namanya your_database_name
        self.collection = self.db["logs"]

    def insert_log(self, log_data: dict):
        result = self.collection.insert_one(log_data)
        return str(result.inserted_id)

    def find_log_by_id(self, log_id: str):
        document = self.collection.find_one({"_id": ObjectId(log_id)})
        if document:
            document["_id"] = str(document["_id"])
        return document
