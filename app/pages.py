from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)


@bp.route("/")
@bp.route("/home")
def home():
    return render_template("home.html")

