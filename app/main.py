from fastapi import FastAPI
import os
from dotenv import load_dotenv
from fetcher.fetcher import fetch_objects, fetch_solar_weather


load_dotenv()
API_KEY = os.environ['API_KEY']

app = FastAPI()

@app.get('/')
def welcome():
    return {'welcome': 'it works'}

@app.get('/asteroids')
def fetch_asteroids():
    
    start_date = "2025-08-14"
    end_date = "2025-08-14"
    
    return fetch_objects(start_date, end_date, API_KEY)

@app.get('/flares')
def fetch_solar_events():
    startDate = "2025-01-01"
    endDate = "2025-01-30"
    
    return fetch_solar_weather(startDate=startDate, endDate=endDate, API_KEY=API_KEY)