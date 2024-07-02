""" 
Módulo que configura y crea la aplicación FastAPI principal
"""

import os
from fastapi import FastAPI
from app.routers import items
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Items API", description="API for managing items", version="1.0.0")

# Configura orígenes permitidos para CORS
origins = os.getenv("CORS_ORIGINS", "http://localhost,http://localhost:8080").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items.router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Items API"}
