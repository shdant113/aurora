from fastapi import APIRouter

from service.sunspots import get_sunspot_regions

solar_activity_router = APIRouter()

@solar_activity_router.get('/sunspots')
async def get_sunspots():
    collected_data = get_sunspot_regions()
    if len(collected_data) > 0:
        return collected_data
    else:
        return {"message": "No data available for sunspot regions"}
    