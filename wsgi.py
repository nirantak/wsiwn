import os

from main import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port)

    app.config.update(
        JSONIFY_PRETTYPRINT_REGULAR=True, SECRET_KEY=os.environ.get("SECRET_KEY")
    )
