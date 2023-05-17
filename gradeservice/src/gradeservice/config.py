from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    assignments_path: Path = Path().cwd()
    jwt_secret: str = ""


settings = Settings()
