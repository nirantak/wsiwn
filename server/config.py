import os

PROJECT_ROOT: str = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
PORT: int = int(os.environ.get("PORT", 5000))
SECRET_KEY: str = os.environ.get("SECRET_KEY", "dev-key")
