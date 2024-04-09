from fastapi import APIRouter, HTTPException
from bson import ObjectId

from config.database import projects_collection
from schema.schemas import list_project

from models.project import Project

project_router = APIRouter()


# LIST ALL THE PROJECTS


@project_router.get("/projects")
async def get_projects():
    projects = list_project(projects_collection.find())

    if projects:
        return projects
    else:
        return {"message": "No projects found"}


# CREATE PROJECT


@project_router.post("/project")
async def create_project(project: Project):
    result = projects_collection.insert_one(dict(project))

    if result.inserted_id:
        return {"message": "Project created successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to create project")


# UPDATE PROJECT


@project_router.put("/project/{id}")
async def update_project(id: str, project: Project):
    result = projects_collection.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(project)}
    )

    if result:
        return {"message": "Project updated successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to update project")


# DELETE PROJECT


@project_router.delete("/project/{id}")
async def delete_project(id: str, project: Project):
    result = projects_collection.find_one_and_delete({"_id": ObjectId(id)})

    if result:
        return {"message": "Project deleted successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to delete project")
