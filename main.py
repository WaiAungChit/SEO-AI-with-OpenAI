from fastapi import FastAPI
import routers.route as generate_routes

app = FastAPI()

app.include_router(generate_routes.router)
