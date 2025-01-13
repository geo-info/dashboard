import uuid
from datetime import datetime, timezone

from typing import Any
from geoalchemy2 import Geometry
from sqlmodel import Field, Column, SQLModel, Relationship


class BaseMixin(SQLModel):

    created_at: datetime | None = Field(
        default_factory = lambda: datetime.now(timezone.utc),
        nullable = False,
    )

    updated_at: datetime | None = Field(
        default_factory = lambda: datetime.now(timezone.utc),
        nullable = False,
        sa_column_kwargs = {
            "onupdate": lambda: datetime.now(timezone.utc),
        }
    )
    __table_args__ = {"schema": 'content'}


class Country(BaseMixin, table = True):
    id: uuid.UUID = Field(default_factory = uuid.uuid4, primary_key = True)
    name: str = Field(min_length = 1, max_length = 255, unique = True)

    subject: list["Subject"] = Relationship(back_populates = "country")


class Subject(BaseMixin, table = True):
    id: uuid.UUID = Field(default_factory = uuid.uuid4, primary_key = True)
    name: str = Field(index=True)

    geometry: Any = Field(sa_column = Column(Geometry("GEOMETRY", srid = 4326)))

    country_id: uuid.UUID | None = Field(default = None, foreign_key = "content.country.id")
    country: Country | None = Relationship(back_populates = "subjects")
