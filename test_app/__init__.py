#!.venv/bin/python
import os
from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(
            SECRET_KEY = 'dev',
            DATABASE = os.path.join(app.instance_path, 'test_app.sqlite')
            )

    app.config.from_pyfile('config.py', silent = True)

    if not os.path.exists(app.instance_path):
        os.makedirs(app.instance_path)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    import test_app.sw
    app.register_blueprint(sw.bp)

    return app

