from fastapi import FastAPI
from fastapi_pagination import add_pagination
from modules.routers import root, pokemon, datascience, get_user
from modules import security

app = FastAPI()

routers = [
    root.router,
    security.router,
    get_user.router,
    pokemon.router,
    datascience.router
]

for router in routers:
    app.include_router(router)

add_pagination(app)
