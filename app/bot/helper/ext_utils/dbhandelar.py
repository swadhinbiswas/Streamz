from aiofiles import open as aiopen
from aiofiles.os import path as aiopath,makedirs
from dotenv import load_dotenv,dotenv_values
from  motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import PyMongoError
from app.settings.config import MONGO_DB_URI,USER_DATA,LOGGER

class DbManager:
  def __init__(self):
    self._err=False
    self._db=None
    self._conn=None
    self._connect()
    
    def connect(self):
        try:
            self._conn = AsyncIOMotorClient(DATABASE_URL)
            self._db = self._conn.mltb
        except PyMongoError as e:
            LOGGER.error(f"Error in DB connection: {e}")
            self._err = True
            
      
    async def close(self):
        if self._conn:
            self._conn.close()
            LOGGER.info("DB Connection Closed")
    
    async def get_metadata(self):
       return await self._db.metadata.find_all()





if MONGO_DB_URI:
  bot_loop.run_until_complete(DbManager().connect())
