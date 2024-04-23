from app import setting
# ,STREAMTAPEAPIKEY,STREAMTAPEUSERAGENT
import requests
from fastapi import APIRouter, File, UploadFile, Form,FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app=FastAPI()
router = APIRouter()

@app.get("userinfo")
async def userinfo():
    url=f"https://doodapi.com/api/account/info?key={DOODAPIKEY}"
    response = requests.get(url)
    return response.json()
  
  
  


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)