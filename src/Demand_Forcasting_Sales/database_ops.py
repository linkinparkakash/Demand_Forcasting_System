import csv
import logging
from pymongo import MongoClient

class MongoCSV:
    def __init__(self, uri, db_name, collection_name):
        self.uri = uri
        self.db_name = db_name
        self.collection_name = collection_name
        self.client = MongoClient(self.uri)

    def upload_csv(self, file_path):
        try:
            db = self.client[self.db_name]
            collection = db[self.collection_name]

            with open(file_path, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                collection.insert_many(reader)

            print("Data uploaded successfully to MongoDB!")
        except Exception as e:
            logging.basicConfig(filename='logs.txt', level=logging.ERROR,
                                format='%(asctime)s %(levelname)s:%(message)s')
            logging.error(str(e))

    def download_csv(self, file_path):
        try:
            db = self.client[self.db_name]
            collection = db[self.collection_name]

            cursor = collection.find()
            with open(file_path, 'w') as csvfile:
                writer = csv.writer(csvfile)
                for document in cursor:
                    writer.writerow(document.values())

            print("Data downloaded successfully to CSV!")
        except Exception as e:
            logging.basicConfig(filename='logs.txt', level=logging.ERROR,
                                format='%(asctime)s %(levelname)s:%(message)s')
            logging.error(str(e))
