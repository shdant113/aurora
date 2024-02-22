from fastapi import FastAPI
from api.v1.ace import ace_router
from api.v1.discover import discover_router
from api.v1.k_index import k_index_router
from api.v1.solar_activity import solar_activity_router

app = FastAPI()

app.include_router(ace_router, prefix='/v1', tags=['ace'])
app.include_router(discover_router, prefix='/v1', tags=['dscovr'])
app.include_router(k_index_router, prefix='/v1', tags=['k-index'])
app.include_router(solar_activity_router, prefix='/v1', tags=['flares', 'sunspots'])

@app.get('/')
async def health():
    return 200
