from typing import Union
import requests

def get_k_index_boulder() -> Union[dict, None]:
    url = "https://services.swpc.noaa.gov/json/boulder_k_index_1m.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from {url}")
        return None    
    
def get_k_index_next_hour() -> Union[dict, None]:
    url = "https://services.swpc.noaa.gov/json/geospace/geospace_pred_est_kp_1_hour.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from {url}")
        return None    
    