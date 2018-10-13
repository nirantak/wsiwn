import os

from flask import Flask, abort, jsonify, make_response, render_template, request
from pyswip import Prolog

from server import config
from server.prolog import search

app = Flask(
    __name__,
    static_url_path="",
    static_folder=os.path.join(config.PROJECT_ROOT, "static"),
    template_folder=os.path.join(config.PROJECT_ROOT, "templates"),
)

swipl = Prolog()

swipl.consult(os.path.join(config.PROJECT_ROOT, "prolog/movies.pl"))
swipl.consult(os.path.join(config.PROJECT_ROOT, "prolog/tv.pl"))


@app.errorhandler(400)
def bad_request(error):
    """400 Error - Bad Request from User"""
    return make_response(jsonify({"error": "Bad request"}), 400)


@app.errorhandler(404)
def not_found(error):
    """404 Error - Resource not found"""
    return make_response(jsonify({"error": "Not found"}), 404)


@app.route("/")
def index():
    """Render Home Page"""
    return render_template("index.html")


@app.route("/movies", methods=["GET", "POST"])
def find_movie():
    """
    GET Request  - Find list of movies matching the query string
    POST Request - Find list of movies matching all given input parameters
    """
    if request.method == "GET":
        if not request.args or "query" not in request.args:
            abort(400)

        query: str = request.args.get("query").lower()
        if not query.isidentifier() and not query.isdecimal():
            abort(400)

        movies = search(swipl, "movie", query)
        return jsonify({"movies": movies}), 200

    if request.method == "POST":
        return jsonify({}), 200

    return jsonify({"error": "Method Not Allowed"}), 405


@app.route("/tv", methods=["GET", "POST"])
def find_tv():
    """
    GET Request  - Find list of TV shows matching the query string
    POST Request - Find list of TV shows matching all given input parameters
    """
    if request.method == "GET":
        if not request.args or "query" not in request.args:
            abort(400)

        query: str = request.args.get("query").lower()
        if not query.isidentifier() and not query.isdecimal():
            abort(400)

        tv = search(swipl, "tv", query)
        return jsonify({"tv": tv}), 200

    if request.method == "POST":
        return jsonify({}), 200

    return jsonify({"error": "Method Not Allowed"}), 405


if __name__ == "__main__":
    app.run(port=config.PORT)
    app.config.update(JSONIFY_PRETTYPRINT_REGULAR=True, SECRET_KEY=config.SECRET_KEY)