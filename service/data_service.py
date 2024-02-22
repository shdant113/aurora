from typing import Union
import requests
from datetime import datetime, timedelta

WIND_URL = "https://services.swpc.noaa.gov/json/rtsw/rtsw_wind_1m.json"
MAG_URL = "https://services.swpc.noaa.gov/json/rtsw/rtsw_mag_1m.json"

def get_data(url) -> Union[dict, None]:
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from {url}")
        return None

def collect_wind_data(source, two_hours_ago) -> list:
    data = []

    response = get_data(WIND_URL)
    if not response:
        return []
    
    ## SWPC gives data tagged every minute
    for minute in response:
        time_tag = datetime.strptime(minute['time_tag'], '%Y-%m-%dT%H:%M:%S')

        ## return only last two hours of data for given source
        if two_hours_ago <= time_tag:
            satellite_name = minute['source']
            if satellite_name == source:
                data.append(minute)

    return data

def collect_solar_data(source, two_hours_ago) -> list:
    data = []

    response = get_data(MAG_URL)
    if not response:
        return []
    
    ## SWPC gives data tagged every minute
    for minute in response:
        time_tag = datetime.strptime(minute['time_tag'], '%Y-%m-%dT%H:%M:%S')

        ## return only last two hours of data for given source
        if two_hours_ago <= time_tag:
            satellite_name = minute['source']
            if satellite_name == source:
                data.append(minute)

    return data

def collect_data(source) -> list:
    data = []
    combined_data = []

    ## Get wind and solar data separate - SWPC publishes two pages
    two_hours_ago = datetime.utcnow() - timedelta(hours=2)

    wind_data = collect_wind_data(source, two_hours_ago)
    solar_data = collect_solar_data(source, two_hours_ago)

    ## Combine data for each timestamp
    for wind_entry in wind_data:
        for solar_entry in solar_data:
            if wind_entry['time_tag'] == solar_entry['time_tag']:
                combined_entry = {**wind_entry, **solar_entry}
                combined_data.append(combined_entry)

    ## Parse data to whatever relevant fields desired
    relevant_fields = ['time_tag', 'proton_speed', 'proton_temperature', 'proton_density', 'bt', 'bz_gsm']
    for entry in combined_data: 
        for key in list(entry.keys()):
            if key not in relevant_fields:
                del entry[key]

        data.append(entry)

    return data
