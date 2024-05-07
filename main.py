from fastapi import FastAPI
from routes.dev_router import dev_router
from routes.project_router import project_router
from routes.freelances_router import freelances_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],  
)

# DEV ROUTER

app.include_router(dev_router)

# PROJECT ROUTER

app.include_router(project_router)

# FREELANCER ROUTER

app.include_router(freelances_router)
