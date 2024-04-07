from fastapi import APIRouter, HTTPException
from bson import ObjectId

from config.database import developers_collection
from schema.schemas import list_dev, list_devs

from models.developer import Developer

dev_router = APIRouter()


# LIST ALL THE DEVELOPERS

@dev_router.get('/developers')
async def get_devs():
  devs = list_devs(developers_collection.find())
  
  if devs:
    return devs
  else:
    return {"message": "No developers found"}
  

# LIST THE FIRST DEVELOPER

@dev_router.get('/developer')
async def get_dev():
  dev = list_dev(developers_collection.find())

  if dev:
    return dev
  else:
    return {"message": "No developers found"}


#CREATE DEVELOPER

@dev_router.post('/developer')
async def create_dev(dev: Developer):
  result = developers_collection.insert_one(dict(dev))

  if result.inserted_id:
    return {"message": "Developer created successfully"}
  else:
    raise HTTPException(status_code=500, detail="Failed to create developer")
  

# UPDATE DEVELOPER

@dev_router.put('/developer/{id}')
async def update_dev(id: str, dev: Developer):
  result = developers_collection.find_one_and_update({'_id': ObjectId(id)}, {'$set': dict(dev)})

  if result:
    return {"message": "Developer updated successfully"}
  else:
    raise HTTPException(status_code=500, detail="Failed to update developer")


#DELETE DEVELOPER

@dev_router.delete('/developer/{id}')
async def delete_dev(id: str, dev: Developer):
  result = developers_collection.find_one_and_delete({"_id": ObjectId(id)})

  if result:
    return {"message": "Developer delete successfully"}
  else:
    raise HTTPException(status_code=500, detail="Failed to delete developer")