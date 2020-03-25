#!/bin/sh
source .venv/bin/activate
export FLASK_APP=test_app
export FLASK_ENV=development
flask run
