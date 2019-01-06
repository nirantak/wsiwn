import os

from flask import Flask
from pyswip import Prolog

from .config import Config

swipl = Prolog()


def create_app(config_class=Config):
    app = Flask(
        __name__,
        static_url_path="",
        static_folder=os.path.join(Config.PROJECT_ROOT, "client"),
    )
    app.config.from_object(Config)

    swipl.consult(os.path.join(Config.PROJECT_ROOT, "server/prolog/movies.pl"))
    swipl.consult(os.path.join(Config.PROJECT_ROOT, "server/prolog/tv.pl"))

    from .routes import router

    app.register_blueprint(router)

    return app
