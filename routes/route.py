from fastapi import APIRouter, HTTPException
from bson import ObjectId

from config.database import collection_name
from schema.schemas import list_experience, list_project, list_dev, list_devs

from models.developer import Developer
from models.experience import Experience
from models.project import Project

router = APIRouter()


# LIST ALL THE DEVELOPERS
@router.get('/developers')
async def get_devs():
  devs = list_devs(collection_name.find())
  if devs:
    return devs
  else:
    return {"message": "No developers found"}
  

# LIST THE FIRST DEVELOPER
@router.get('/developer')
async def get_dev():
  dev = list_dev(collection_name.find())
  if dev:
    return dev
  else:
    return {"message": "{dev} wasn't found"}


#CREATE DEVELOPER

@router.post('/developer')
async def create_dev(dev: Developer):
  result = collection_name.insert_one(dict(dev))

  if result.inserted_id:
    return {"message": "Developer created successfully"}
  else:
    raise HTTPException(status_code=500, detail="Failed to create developer")