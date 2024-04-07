from fastapi import FastAPI
from routes.dev_router import dev_router
from routes.exp_router import exp_router
from routes.project_router import project_router

app=FastAPI()

# DEV ROUTER

app.include_router(dev_router)

# EXP ROUTER

app.include_router(exp_router)

# PROJECT ROUTER

app.include_router(project_router)