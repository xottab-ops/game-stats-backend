from flask import Blueprint

healthcheck_bp = Blueprint("health", __name__, url_prefix="/health")

@healthcheck_bp.route("", methods=["GET"])
def healthcheck():
    return {"status": "ok"}, 200