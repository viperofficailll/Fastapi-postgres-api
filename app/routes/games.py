from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.game import (
    GameCreate,
    GameUpdate,
    GameResponse
)

from app.services import games


router = APIRouter(
    prefix="/games",
    tags=["Games"]
)


@router.get(
    "",
    response_model=list[GameResponse]
)
def get_games(
    db: Session = Depends(get_db)
):
    return games.get_games(db)



@router.get(
    "/{game_id}",
    response_model=GameResponse
)
def get_game(
    game_id: int,
    db: Session = Depends(get_db)
):
    return games.get_game(
        db,
        game_id
    )



@router.post(
    "",
    response_model=GameResponse
)
def create_game(
    game_data: GameCreate,
    db: Session = Depends(get_db)
):
    return games.create_game(
        db,
        game_data
    )



@router.put(
    "/{game_id}",
    response_model=GameResponse
)
def update_game(
    game_id: int,
    game_data: GameUpdate,
    db: Session = Depends(get_db)
):
    return games.update_game(
        db,
        game_id,
        game_data
    )



@router.delete(
    "/{game_id}",
    response_model=GameResponse
)
def delete_game(
    game_id: int,
    db: Session = Depends(get_db)
):
    return games.delete_game(
        db,
        game_id
    )