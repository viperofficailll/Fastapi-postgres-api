from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories import games as repository
from app.schemas.game import GameCreate, GameUpdate


def get_games(
    db: Session,
    genre: str | None = None,
    name: str | None = None,
    sort_by: str | None = None,
    order: str = "asc",
):
    return repository.get_games(
        db=db,
        genre=genre,
        name=name,
        sort_by=sort_by,
        order=order,
    )


def get_game(
    db: Session,
    game_id: int
):

    game = repository.get_game_by_id(
        db,
        game_id
    )

    if not game:
        raise HTTPException(
            status_code=404,
            detail="Game not found"
        )

    return game


def create_game(
    db: Session,
    game_data: GameCreate
):

    return repository.create_game(
        db,
        game_data
    )


def update_game(
    db: Session,
    game_id: int,
    game_data: GameUpdate
):

    game = get_game(
        db,
        game_id
    )

    return repository.update_game(
        db,
        game,
        game_data
    )


def delete_game(
    db: Session,
    game_id: int
):

    game = get_game(
        db,
        game_id
    )

    repository.delete_game(
        db,
        game
    )

    return None