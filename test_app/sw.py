from flask import (
        Blueprint, make_response, send_from_directory
)

bp = Blueprint('sw', __name__, url_prefix='')

@bp.route('/sw.js')
def service_worker():
    response = make_response(send_from_directory('static', 'sw.js'))
    response.headers['Cache-Control'] = 'no-cache'
    return response
