import os
from pathlib import Path

from typing import Any

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import (
    Field, model_validator
)

BASE_DIR = Path(os.path.dirname(os.path.dirname(__file__)))


def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class Base(BaseSettings):

    model_config = SettingsConfigDict(
        env_file = os.path.join(BASE_DIR.parent.parent, '.env'),
        env_file_encoding = 'utf-8',
    )


class PostgresSettings(Base):
    protocol: str = "postgresql+psycopg"
    username: str = 'admin'
    password: str = 'admin'
    host: str = '127.0.0.1'
    port: int = 5432

    path: str = Field(validation_alias = "POSTGRES_DB")
    schemas: str = "content"
    pool_recycle: int = 1800

    dsn: str = ''

    @model_validator(mode='after')
    def create_dsn(self) -> 'PostgresSettings':
        self.dsn = "{protocol}://{username}:{password}@{host}:{port}/{path}".format(
            username = self.username,
            password = self.password,
            protocol = self.protocol,
            host = self.host,
            port = self.port,
            path = self.path,
        )
        return self
#
    model_config = SettingsConfigDict(
        env_prefix = 'POSTGRES_', extra = 'ignore'
    )

class UvicornSettings(Base):
    app: str = "app.main:app"
    host: str = "127.0.0.1"
    port: int = 8000
    reload: bool = True
    workers: int = 3

    model_config = SettingsConfigDict(
        env_prefix = 'UVICORN_', extra = 'ignore'
    )


class Settings(BaseSettings):

    uvicorn: UvicornSettings = UvicornSettings()
    postgis: PostgresSettings = PostgresSettings()


settings: Settings = Settings()  # type: ignore
