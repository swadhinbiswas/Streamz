import requests
import re
import sys
import asyncio 

from typing import Optional

class DoodStream:
    def __init__(self,api_key:str):
        self.api_key=api_key
        self.base_url="https://doodapi.com/api"
        self.headers={"Content-Type":"application/json"}
        
    def _req(self,url:str)->dict:
          try:
            r=requests.get(url)
            response=r.json()
            if response["msg"]=="Wrong API Key":
              Exception("Invalid API Key")
            else:
              return response
          except Exception as e:
            Exception(e)
            
    def userinfo(self)->dict:
        url=f"{self.base_url}/account/info?key={self.api_key}"
        return self._req(url)
    
    def account_reports(self,
                        last:Optional[str]=None,
                        from_date:Optional[str]=None,
                        to_date:Optional[str]=None,)->dict:
        url=f"{self.base_url}/account/stats?key={self.api_key}"
        if last != None:
            url += f"&last={last}"
        if from_date != None:
            url = f"&from_date={from_date}"
        if to_date != None:
            url = f"&to_date={to_date}"
        url = f"{self.base_url}account/stats?key={self.api_key}"
        return self._req(url)
    
    def dmca_list(
      self,per_page:Optional[int]=None,
      page:Optional[int]=None)->dict:
        url=f"{self.base_url}/dmca/list?key={self.api_key}"
        if per_page != None:
            url += f"&per_page={per_page}"
        if page != None:
            url += f"&page={page}"
        return self._req(url)
      
    async def upload_video(self,path)->dict:
        url = f"{self.base_url}upload/server?key={self.api_key}"
        url_for_upload = self._req(url)["result"]
        post_data = {"api_key": self.api_key}
        filename = path.split("/")[-1]
        post_files = {"file": (filename, open(path, "rb"))}
        res = requests.post(url_for_upload, data=post_data, files=post_files).json()
        if res["msg"] == "OK":
            return res
        else:
            raise TypeError(
                f"unsupported video format {filename}, please upload video with mkv, mp4, wmv, avi, mpeg4, mpegps, flv, 3gp, webm, mov, mpg & m4v format"
            )
    
    def copy_video(self,file_code:str,file_id:Optional[str]=None)->dict:
        url=f"{self.base_url}/video/copy?key={self.api_key}&file_code={file_code}"
        if file_id != None:
            url += f"&file_id={file_id}"
        return self._req(url)
    
    def remote_upload(
        self,
        direct_link: str,
        fild_id: Optional[str] = None,
        file_name: Optional[str] = None,)->dict:
        url = f"{self.base_url}/upload/remote?key={self.api_key}"
        return self._req(url)
    
    def remote_upload_status(self,file_code:str)->dict:
        url=f"{self.base_url}/upload/status?key={self.api_key}&file_code={file_code}"
        return self._req(url)
    
    def remote_upload_slots(self)->dict:
        url=f"{self.base_url}/upload/slots?key={self.api_key}"
        return self._req(url)
    
    def remote_upload_action(
        self,
        restart_error:bool,
        clear_error:Optional[bool]=None,
        clear_completed:Optional[bool]=None,
        clear_all:Optional[bool]=None,)->dict:
        url = f"{self.base_url}urlupload/actions?key={self.api_key}&restart_errors={restart_error}"
        if clear_error != None:
            url += f"&clear_errors={clear_error}"
        if clear_completed != None:
            url += f"&clear_completed={clear_completed}"
        if clear_all != None:
            url += f"&clear_all={clear_all}"
        return self._req(url)
    
    def create_folder(self,name:str,parent_id:Optional[str]=None)->dict:
        url=f"{self.base_url}/folder/create?key={self.api_key}&name={name}"
        if parent_id != None:
            url += f"&parent_id={parent_id}"
        return self._req(url)
    
    def list_files(self,
                  page:Optional[int]=None,
                  per_page:Optional[int]=None,
                  parent_id:Optional[str]=None)->dict:
        url=f"{self.base_url}/files/list?key={self.api_key}"
        if page != None:
            url += f"&page={page}"
        if per_page != None:
            url += f"&per_page={per_page}"
        if parent_id != None:
            url += f"&parent_id={parent_id}"
        return self._req(url)
    
    def delete_file(self,file_id:str)->dict:
        url=f"{self.base_url}/file/delete?key={self.api_key}&file_id={file_id}"
        return self._req(url)
    
    def get_file_info(self,file_id:str)->dict:
        url=f"{self.base_url}/file/info?key={self.api_key}&file_id={file_id}"
        return self._req(url)

    def rename_file(self,file_id:str,name:str)->dict:
        url=f"{self.base_url}/file/rename?key={self.api_key}&file_id={file_id}&name={name}"
        return self._req(url)

    def move_file(self,file_id:str,parent_id:str)->dict:
        url=f"{self.base_url}/file/move?key={self.api_key}&file_id={file_id}&parent_id={parent_id}"

        return self._req(url)

    def delete_folder(self,folder_id:str)->dict:
        url=f"{self.base_url}/folder/delete?key={self.api_key}&folder_id={folder_id}"
        return self._req(url)


    def copy_file(self,file_id:str,parent_id:str)->dict:
        url=f"{self.base_url}/file/copy?key={self.api_key}&file_id={file_id}&parent_id={parent_id}"
        return self._req(url)
    
    
    def file_info(self,file_id:str)->dict:
        url=f"{self.base_url}/file/info?key={self.api_key}&file_id={file_id}"
        return self._req(url)
    
    
    def file_serach(self,query:str)->dict:
        url=f"{self.base_url}/files/search?key={self.api_key}&query={query}"
        return self._req(url)

    



