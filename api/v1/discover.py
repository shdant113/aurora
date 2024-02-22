from service.data_service import collect_data

from fastapi import APIRouter

discover_router = APIRouter()

@discover_router.get('/data/discover')
async def discover_data():
    collected_data = collect_data("DSCOVR")
    if len(collected_data) > 0:
        return collected_data
    else:
        return {"message": "No data available for DSCOVR"}
