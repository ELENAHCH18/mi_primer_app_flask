from flask import Flask # type: ignore

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app