from src.config.base import setings
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from src.controller.generate_mvt_controller import NewMvtController
from src.controller.generate_geojson_controller import NewGeojsonController

from fastapi import FastAPI

app = FastAPI(
    title="Map Layer Svc",
    description="Try Maps Layer",
    # openapi_tags="MVT"
)
app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(NewMvtController().GetRouter())
app.include_router(NewGeojsonController().GetRouter())

if __name__ == "__main__":
    port = setings.SERVICE_PORT
    if not port:
        port="8000"
    uvicorn.run(app, host="0.0.0.0", port=int(port))