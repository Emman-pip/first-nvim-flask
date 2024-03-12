from flask import Flask

from .models import db
from .pages import bp as pages


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///somedatabase.db"
    db.init_app(app)

    app.register_blueprint(pages)

    return app

