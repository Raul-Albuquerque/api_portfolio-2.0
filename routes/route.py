from fastapi import APIRouter
from bson import ObjectId

from config.database import collection_name
from schema.schemas import list_experience, list_project

from models.developer import Developer
from models.experience import Experience
from models.project import Project

router = APIRouter()


