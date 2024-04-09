from fastapi import APIRouter, HTTPException
from bson import ObjectId

from config.database import experiences_collection
from schema.schemas import list_experience

from models.experience import Experience

exp_router = APIRouter()


# LIST ALL THE EXPERIENCES


@exp_router.get("/experience")
async def get_experiences():
    experiences = list_experience(experiences_collection.find())

    if experiences:
        return experiences
    else:
        return {"message": "No experiences found"}


# CREATE EXPERIENCE


@exp_router.post("/experience")
async def create_exp(exp: Experience):
    result = experiences_collection.insert_one(dict(exp))

    if result.inserted_id:
        return {"message": "Experience created successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to create experience")


# UPDATE EXPERIENCE


@exp_router.put("/experience/{id}")
async def update_exp(id: str, exp: Experience):
    result = experiences_collection.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(exp)}
    )

    if result:
        return {"message": "Experience updated successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to update experience")


# DELETE EXPERIENCE


@exp_router.delete("/experience/{id}")
async def delete_exp(id: str, exp: Experience):
    result = experiences_collection.find_one_and_delete({"_id": ObjectId(id)})

    if result:
        return {"message": "Experience deleted successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to delete experience")
