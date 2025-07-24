from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI()

# Explicitly using absolute path
DATA_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data.csv'))

@app.get('/get_csv_data')
async def get_csv_data():
    df = pd.read_csv(DATA_FILE)
    return df.to_dict(orient='records')
