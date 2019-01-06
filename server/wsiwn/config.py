import os


class Config:
    DEBUG: bool = False
    PORT: int = int(os.environ.get("PORT", 5000))
    PROJECT_ROOT: str = os.path.abspath(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    )
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "dev-key")
