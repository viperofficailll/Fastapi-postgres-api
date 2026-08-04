from pydantic import BaseModel, ConfigDict, Field


class GameBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)

    genre: str = Field(..., min_length=2, max_length=50)

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)


class GameCreate(GameBase):
    pass


class GameUpdate(GameBase):
    pass


class GameResponse(GameBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
