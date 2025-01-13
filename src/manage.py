import typer
import uvicorn
import asyncio

from functools import wraps
from typing import Callable, Any

from app.core.settings import settings

typer_app = typer.Typer()


def coro(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        return asyncio.run(func(*args, **kwargs))

    return wrapper


@typer_app.command()
def runserver():
    uvicorn.run(
        **settings.uvicorn.model_dump(),
    )


if __name__ == "__main__":
    typer_app()
