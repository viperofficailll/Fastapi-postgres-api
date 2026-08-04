from sqlalchemy.orm import Session

from app.models.games import Game
from app.schemas.game import GameCreate, GameUpdate


def get_games(
    db: Session,
    genre: str | None = None,
    name: str | None = None,
    sort_by: str | None = None,
    order: str = "asc",
):
    query = db.query(Game)

    if genre:
        query = query.filter(Game.genre.ilike(f"%{genre}%"))

    if name:
        query = query.filter(Game.name.ilike(f"%{name}%"))

    if sort_by in {"id", "name", "genre"}:
        sort_column = getattr(Game, sort_by)
        if order == "desc":
            query = query.order_by(sort_column.desc())
        else:
            query = query.order_by(sort_column.asc())

    return query.all()


def get_game_by_id(db: Session, game_id: int):
    return (
        db.query(Game)
        .filter(Game.id == game_id)
        .first()
    )


def create_game(
    db: Session,
    game_data: GameCreate
):
    game = Game(
        name=game_data.name,
        genre=game_data.genre
    )

    db.add(game)
    db.commit()
    db.refresh(game)

    return game


def update_game(
    db: Session,
    game: Game,
    game_data: GameUpdate
):

    game.name = game_data.name
    game.genre = game_data.genre

    db.commit()
    db.refresh(game)

    return game


def delete_game(
    db: Session,
    game: Game
):

    db.delete(game)
    db.commit()

    return game