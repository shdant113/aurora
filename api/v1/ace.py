from service.rtsw import collect_data

from fastapi import APIRouter

ace_router = APIRouter()

@ace_router.get("/data/ace")
async def ace_data():
    collected_data = collect_data("ACE")
    if len(collected_data) > 0:
        return collected_data
    else:
        return {"message": "No data available for ACE"}
