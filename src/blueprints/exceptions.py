from flask import Blueprint, render_template

exc = Blueprint("exception", __name__)


@exc.app_errorhandler(404)
def page_not_found(e):
    return render_template("exceptions/404.html"), 404
