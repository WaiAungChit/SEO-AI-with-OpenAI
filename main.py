from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import routers.route as generate_routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(generate_routes.router)
