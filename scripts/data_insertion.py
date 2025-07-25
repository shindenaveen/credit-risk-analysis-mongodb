import pandas as pd
from pymongo import MongoClient

# Load your CSV data into a pandas DataFrame
df = pd.read_csv('credit_risk_data.csv')

# Convert DataFrame to list of dictionaries
records = df.to_dict('records')

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Access (or automatically create) your database and collection
db = client['credit_db']
collection = db['credit_data']

# Insert all records
collection.insert_many(records)

print(f"Inserted {len(records)} records into MongoDB.")
