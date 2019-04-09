from typing import Dict

from flask import Blueprint, abort, jsonify, make_response, request

from .__init__ import swipl
from .prolog import advance_search, search

router = Blueprint("router", __name__)


@router.app_errorhandler(400)
def error_400(error):
    """400 Error - Bad Request from User"""
    return make_response(jsonify({"error": "Bad request", "code": 400}), 400)


@router.app_errorhandler(404)
def error_404(error):
    """404 Error - Resource not found"""
    return make_response(jsonify({"error": "URI Not found", "code": 404}), 404)


@router.route("/api/<category>", methods=["GET", "POST"])
def watchlist(category: str):
    """
    category     - One of {movies, tv}
    GET Request  - Find list of movies/tv matching the query string
    POST Request - Find list of movies/tv matching all given input parameters
    """
    category = category.lower()
    if category not in {"movies", "tv"}:
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

    return jsonify({"error": "Method Not Allowed", "code": 405}), 405
