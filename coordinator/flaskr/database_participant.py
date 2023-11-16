from pymongo import MongoClient

class DatabaseParticipant:
    def __init__(self, database_url, database_name, collection_name):
        self.client = MongoClient(database_url)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def prepare(self):
        # Perform prepare actions, return 'YES' or 'ABORT' based on conditions
        # Check if the required data exists in the collection
        if self.collection.find_one({"key": "value"}):
            return 'YES'
        else:
            return 'ABORT'

    def commit(self):
        # Perform commit actions in the MongoDB collection
        document_to_insert = {"key": "value", "another_key": "another_value"}
        self.collection.insert_one(document_to_insert)

    def abort(self):
        # Perform abort actions in the MongoDB collection
        # Remove data from the collection
        # Deleting the document that was inserted during the commit phase
        self.collection.delete_one({"key": "value"})
