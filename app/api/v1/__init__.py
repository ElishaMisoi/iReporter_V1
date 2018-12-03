# from flask import Blueprint, Flask
# from app.api.v1.views import create_incident
 
# vers = Flask(__name__)
# app.register_blueprint(create_incident)

# version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')

# api = Api(version_one)

# api.add_resource(Incident, '/incidents/<int:incident_id>')
# api.add_resource(IncidentList, '/incidents')
# api.add_resource(IncidenceQuery, '/incidents/<string:incident_type>')
# api.add_resource(User, '/users/<int:user_id>')
# api.add_resource(UserList, '/users')
# api.add_resource(Register, '/auth/register')