import os
from typing import Dict, Set

from flask import Flask, abort, jsonify, make_response, render_template, request
from pyswip import Prolog

from server import config
from server.prolog import advance_search, search

app = Flask(
    __name__,
    static_url_path="",
    static_folder=os.path.join(config.PROJECT_ROOT, "static"),
    template_folder=os.path.join(config.PROJECT_ROOT, "templates"),
)

swipl = Prolog()

swipl.consult(os.path.join(config.PROJECT_ROOT, "prolog/movies.pl"))
swipl.consult(os.path.join(config.PROJECT_ROOT, "prolog/tv.pl"))

categories: Set[str] = {"movies", "tv"}


@app.errorhandler(400)
def bad_request(error):
    """400 Error - Bad Request from User"""
    return make_response(jsonify({"error": "Bad request"}), 400)


@app.errorhandler(404)
def not_found(error):
    """404 Error - Resource not found"""
    return make_response(jsonify({"error": "URI Not found"}), 404)


@app.route("/")
def index():
    """Render Home Page"""
    return render_template("index.html")


@app.route("/api/<category>", methods=["GET", "POST"])
def watchlist(category: str):
    """
    category     - One of {movies, tv}
    GET Request  - Find list of movies/tv matching the query string
    POST Request - Find list of movies/tv matching all given input parameters
    """
    category = category.lower()
    if category not in categories:
        abort(404)

    # Basic keyword search on GET request
    if request.method == "GET":
        if not request.args or "query" not in request.args:
            abort(400)

        query: str = request.args.get("query").lower()
        if not query.isidentifier() and not query.isdecimal():
            abort(400)

        res = search(swipl, category, query)
        return jsonify({category: res, "count": len(res)}), 200

    # Advanced search on POST request
    if request.method == "POST":
        query: Dict[str, str] = {}

        query["language"] = request.form.get("language")
        query["genre"] = request.form.get("genre")
        query["duration"] = request.form.get("duration")
        query["year"] = request.form.get("year")
        query["seasons"] = request.form.get("seasons")
        query["status"] = request.form.get("status")

        if not any(query.values()):
            abort(400)

        res = advance_search(swipl, category, query)
        return jsonify({category: res, "count": len(res)}), 200

    return jsonify({"error": "Method Not Allowed"}), 405


if __name__ == "__main__":
    app.run(port=config.PORT)
    app.config.update(JSONIFY_PRETTYPRINT_REGULAR=True, SECRET_KEY=config.SECRET_KEY)
