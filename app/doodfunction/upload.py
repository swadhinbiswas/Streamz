from app.setting.config import DOODAPIKEY
# ,STREAMTAPEAPIKEY,STREAMTAPEUSERAGENT
import requests
from fastapi import APIRouter, File, UploadFile, Form,FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter()

@router.get("/userinfo")
async def userinfo():
    url=f"https://doodapi.com/api/account/info?key={DOODAPIKEY}"
    response = requests.get(url)
    return response.json()

@router.get("/accountinfo")
async def accountinfo():
    url=f"https://doodapi.com/api/account/stats?key={DOODAPIKEY}"
    response = requests.get(url)
    return response.json()


@router.get("/dmcainfo")
async def dmcainfo():
    url=f"https://doodapi.com/api/dmca/list?key={DOODAPIKEY}"
    response = requests.get(url)
    return response.json()

@router.post('/remoteupload')
async def remoteupload(url: str = Form(...), folder_id: str = Form(...)):
    url=f"https://doodapi.com/api/remote/upload?key={DOODAPIKEY}&url={url}&folder_id={folder_id}"
    response = requests.post(url)
    return response.json()

@router.post('/upload')
async def upload(file: UploadFile = File(...), folder_id: str = Form(...)):
    url=f"https://doodapi.com/api/upload?key={DOODAPIKEY}&folder_id={folder_id}"
    files = {'file': file.file}
    response = requests.post(url, files=files)
    return response.json()

