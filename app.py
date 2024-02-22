from fastapi import FastAPI
from api.v1.ace import ace_router
from api.v1.discover import discover_router

app = FastAPI()

app.include_router(ace_router, prefix='/v1', tags=['ace'])
app.include_router(discover_router, prefix='/v1', tags=['dscovr'])

@app.get('/')
async def health():
    return 200
