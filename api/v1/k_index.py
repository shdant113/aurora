from service.k_index import get_k_index_boulder, get_k_index_next_hour

from fastapi import APIRouter

k_index_router = APIRouter()

@k_index_router.get('/k/boulder')
async def k_index_boulder():
    collected_data = get_k_index_boulder()
    if len(collected_data) > 0:
        return collected_data
    else:
        return {"message": "No data available for K Index"}


@k_index_router.get('/k/hour')
async def k_index_next_hour():
    collected_data = get_k_index_next_hour()
    if len(collected_data) > 0:
        return collected_data
    else:
        return {"message": "No data available for K Index"}
    