from fastapi import APIRouter, HTTPException
from bson import ObjectId

from config.database import freelances_collection
from schema.schemas import list_freelance

from models.freelance import Freelance

freelances_router = APIRouter()


# LIST ALL THE PROJECTS

@freelances_router.get("/freelances")
async def get_freelances():
    freelances = list_freelance(freelances_collection.find())

    if freelances:
        return freelances
    else:
        return {"message": "No freelances found"}


# CREATE PROJECT

@freelances_router.post("/freelance")
async def create_freelance(freelance: Freelance):
    result = freelances_collection.insert_one(dict(freelance))

    if result.inserted_id:
        return {"message": "Freelance created successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to create freelance")


# UPDATE PROJECT

@freelances_router.put("/freelance/{id}")
async def update_freelance(id: str, freelance: Freelance):
    result = freelances_collection.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(freelance)}
    )

    if result:
        return {"message": "Freelance updated successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to update freelance")


# DELETE PROJECT

@freelances_router.delete("/freelance/{id}")
async def delete_project(id: str, freelance: Freelance):
    result = freelances_collection.find_one_and_delete({"_id": ObjectId(id)})

    if result:
        return {"message": "Freelance deleted successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to delete freelance")
