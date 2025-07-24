from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI()

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data.csv')

@app.get('/api/get_csv_data')
async def get_csv_data():
    df = pd.read_csv(DATA_FILE)
    return df.to_dict(orient='records')