from typing import Union
import requests

def get_sunspot_regions() -> Union[dict, None]:
    url = "https://services.swpc.noaa.gov/json/solar_regions.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from {url}")
        return None    
    