from fastapi import FastAPI
from mangum import Mangum

from app.api.api_v1.api import router as api_router


app = FastAPI()


@app.get("/")
async def root():
    return {"message": f"This is our secret key value" }


app.include_router(api_router)
handler = Mangum(app)
#test
