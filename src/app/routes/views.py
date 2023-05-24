from flask import Blueprint, jsonify
from app.services import service1, service2

bp = Blueprint('views', __name__)

@bp.route('/')
def hello_world():
    return jsonify({"message": "Hello, World!"})

@bp.route('/service1', methods=['POST'])
def do_service1():
    result = service1.run()
    return jsonify(result)

@bp.route('/service2', methods=['GET'])
def do_service2():
    result = service2.run()
    return jsonify(result)
