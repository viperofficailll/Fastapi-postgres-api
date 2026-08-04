from app.app import app
from app.routes.games import router as games_router

app.include_router(games_router)
