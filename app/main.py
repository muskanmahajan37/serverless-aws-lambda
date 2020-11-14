from fastapi import FastAPI
from mangum import Mangum

from app.api.api_v1.api import router as api_router
from app.core.config import settings

app = FastAPI()


@app.get("/")
async def root():
    return {"message": f"Secret key: {settings.db_user}" }



app.include_router(api_router, prefix=settings.prefix)
handler = Mangum(app)
