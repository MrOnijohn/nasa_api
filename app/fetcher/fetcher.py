import requests

def fetch_objects(start_date: str, end_date: str, API_KEY: str) -> dict:
    url = "https://api.nasa.gov/neo/rest/v1/feed"
    params = {"start_date": start_date, "end_date": end_date, "API_KEY": API_KEY}
    
    response = requests.get(url, params)
    response.raise_for_status()

    return response.json()

def fetch_solar_weather(startDate: str, endDate: str, API_KEY: str, event_type:str="all") -> dict:
    url = "https://api.nasa.gov/DONKI/notifications"
    params = {"startDate": startDate, "endDate": endDate, "API_KEY": API_KEY, "type": event_type}

    response = requests.get(url=url, params=params, timeout=10)
    response.raise_for_status()

    return response.json()