import json
from flask import Response

def parse_response(status=200, message="", data=None):
    """
    Returns a response object for DB searches
    """
    if not data:
        data = {}
    data = {
        "message": message,
        "status": status
    }

    return Response(
        response=json.dumps(obj=data),
        status=status,
        mimetype="application/json",
        headers={'access-control-allow-origin': '*'},
    )