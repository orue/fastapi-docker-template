# project/app/main.py

from fastapi import Depends, FastAPI

from app.config import Settings, get_settings

description = """
Boilerplate Project.
 
## Technology
- FastAPI
- Docker
- MongoDB  
"""

app = FastAPI(title="FastAPI Template",
              description=description,
              contact={
                  "name": "Carlos Orue",
                  "url": "https://orue.io"
              })


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
