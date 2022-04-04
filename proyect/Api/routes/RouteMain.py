from flask import Flask, request, jsonify
from flask import Blueprint

import sys
sys.path.append(".")

routes = Blueprint('route',__name__)

class route():

    @routes.route("/", methods=["GET"])
    def login():
        return 'hola mundo'