
from app.setting.config import DOODAPIKEY
# ,STREAMTAPEAPIKEY,STREAMTAPEUSERAGENT
import requests
from fastapi import APIRouter, File, UploadFile, Form,FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.doodfunction.upload import router as doodrouter
app=FastAPI()

app.include_router(doodrouter)

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)