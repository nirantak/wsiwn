from flask import Flask, abort, jsonify, make_response, render_template, request
from pyswip import Prolog

app = Flask(__name__, static_url_path="")
prolog = Prolog()

prolog.consult("prolog/movies.pl")
prolog.consult("prolog/tv.pl")


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": "Bad request"}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/movies", methods=["GET", "POST"])
def find_movie():
    if request.method == "GET":
        if not request.args or "search" not in request.args:
            abort(400)

        q = prolog.query(f"movie(X, {request.args.get('search')})")
        movies = [i["X"].decode("utf-8") for i in list(q)]
        return jsonify({"movies": movies}), 200

    if request.method == "POST":
        return jsonify({}), 200

    return jsonify({"error": "Method Not Allowed"}), 405


@app.route("/tv", methods=["GET", "POST"])
def find_tv():
    if request.method == "GET":
        if not request.args or "search" not in request.args:
            abort(400)

        q = prolog.query(f"tv(X, {request.args.get('search')})")
        tv = [i["X"].decode("utf-8") for i in list(q)]
        return jsonify({"tv": tv}), 200

    if request.method == "POST":
        return jsonify({}), 200

    return jsonify({"error": "Method Not Allowed"}), 405
