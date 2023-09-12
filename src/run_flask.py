from src.api.routes import register_urls
from src.app import app

register_urls(app)


if __name__ == "__main__":
    app.run(debug=True, port=5020)
