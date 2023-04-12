import pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb+srv://nini:<password>@cluster0.un12zr7.mongodb.net/?retryWrites=true&w=majority")
db = client.test

DATA_FILE_PATH = (r"C:/Users/HP/Demand_Forcasting_System_Store_Sales/Demand_Forcasting_System/src/Demand_Forcasting_System/datasets/train.csv")
DATABASE_NAME = "TIMESERIES"
COLLECTION_NAME = "TIMESERIES_PROJECT"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns: {df.shape}")

    df.reset_index(drop = True, inplace = True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

