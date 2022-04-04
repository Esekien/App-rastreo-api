from flask import Flask, request, jsonify
from flask import Blueprint
import json

import sys
sys.path.append(".")

routes = Blueprint('route',__name__)

from proyect.Api.schema.schema import VehiculoSchema 
vehiculo_schema = VehiculoSchema()
vehiculos_schema = VehiculoSchema(many=True)

from proyect import db
from proyect.Api.Models.model import Vehiculo


class route():

    @routes.route("/", methods=["GET"])
    def login():
        return 'hola mundo'

    @routes.route("/view", methods=["GET"])
    def view():
        all_tasks = Vehiculo.query.all()
        result = vehiculos_schema.dump(all_tasks)
        return jsonify(result)

    @routes.route("/create", methods=["POST","GET"])
    def create():

        plates =  request.values.get("plates", type=str, default=None)
        lat =  request.values.get("lat", type=str, default=None)
        lon =  request.values.get("lon", type=str, default=None)

        user_id = 1

        new_vehiculo = Vehiculo(plates, lat, lon, user_id)

        db.session.add(new_vehiculo)
        db.session.commit()

        return jsonify({"message": "vehiculo agregado"}) 
