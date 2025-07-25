from pymongo import MongoClient
import pandas as pd

def load_data_from_mongodb(
    uri="mongodb://localhost:27017/",
    database="credit_db",
    collection="credit_data",
    query={}
):
    client = MongoClient(uri)
    db = client[database]
    coll = db[collection]
    cursor = coll.find(query)
    data = list(cursor)
    for record in data:
        record.pop('_id', None)
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = load_data_from_mongodb()
    df.to_csv("mongo_data.csv", index=False)
