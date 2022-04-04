from flask_marshmallow import Marshmallow
from proyect.Api.Models.model import Vehiculo, User
import sys
sys.path.append(".")
from proyect import app


ma = Marshmallow(app)

class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'full_name')

class VehiculoSchema(ma.Schema):
    class Meta:
        model = Vehiculo
        fields = ('plates', 'lat', 'lon', 'user_id')
