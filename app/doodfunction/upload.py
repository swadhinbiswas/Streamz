from app.setting.config import DOODAPIKEY
from app.doodfunction.doodstream import DoodStream
# ,STREAMTAPEAPIKEY,STREAMTAPEUSERAGENT
import requests
from fastapi import APIRouter, File, UploadFile, Form,FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter()
apicall=DoodStream(DOODAPIKEY)
@router.get("/userinfo")
async def user():
   x=apicall.userinfo()
   return x

@router.get("/accountinfo")
async def accountinfo():
    x= await apicall.account_reports()
    return x



@router.get("/dmcainfo")
async def dmcainfo():
    x= await apicall.dmca_list()
    return x
@router.post('/remoteupload')
async def remoteupload(url: str = Form(...)):
    x=  apicall.remote_upload(url)
    return x


@router.post('/upload')
async def upload(file: UploadFile = File(...)):
    url=f"https://doodapi.com/api/upload?key={DOODAPIKEY}&folder_id={folder_id}"
    files = {'file': file.file}
    response = requests.post(url, files=files)
    return response.json()

