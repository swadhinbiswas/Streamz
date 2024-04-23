from settings import config as config
# ,STREAMTAPEAPIKEY,STREAMTAPEUSERAGENT
import requests
from fastapi import APIRouter, File, UploadFile, Form,FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app=FastAPI()
router = APIRouter()

@app.get("/userinfo")
async def userinfo():
    url=f"https://doodapi.com/api/account/info?key=383661fid15w8jz8w50qza"
    response = requests.get(url)
    return response.json()
  
  
  


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)