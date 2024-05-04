from fastapi import FastAPI
from routes.dev_router import dev_router
from routes.project_router import project_router
from routes.freelances_router import freelances_router

app = FastAPI()

# DEV ROUTER

app.include_router(dev_router)

# PROJECT ROUTER

app.include_router(project_router)

# FREELANCER ROUTER

app.include_router(freelances_router)
