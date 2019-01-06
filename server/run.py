from .wsiwn import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
    app.config.update(JSONIFY_PRETTYPRINT_REGULAR=True)
