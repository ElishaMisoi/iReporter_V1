from flask import Flask, jsonify, request
from app.api.v1.models import Incident, User
from datetime import datetime
app = Flask(__name__)

incidents_list = []

users = []


@app.route('/api/v1/incident', methods=['POST'])
def create_incident():
    # posting an incident
    data = request.get_json()
    id = len(incidents_list)+1
    createdOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    createdBy = id = len(incidents_list)+1
    incident = Incident(id, createdOn, createdBy, data['type'], data['location'],
                data['status'],
                data['Images'], data['Videos'], data['comment'])

    incidents_list.append(incident)

    return jsonify({
        "message": "Incident created",
        "status": 201,
        }), 201


@app.route('/api/v1/incidents', methods=['GET'])
def get_incidents():
    # getting all incidents
    Incidents = [incident.get_incident() for incident in incidents_list]
    return jsonify({"data": Incidents})


@app.route('/api/v1/incidents/<int:incident_id>', methods=['GET'])
def get_incident(incident_id):
    my_incident = []
    incident = incidents_list[incident_id - 1]
    my_incident.append(incident.get_incident())
    return jsonify({
        "data": my_incident
        }), 200



@app.route('/api/v1/incidents/<int:incident_id>', methods=['PUT'])
def edit_record(incident_id):
    # function for editing an incident
    if incident_id == 0 or incident_id > len(incidents_list):
        return jsonify({"message": "Index is out of range"}), 400
    data = request.get_json()
    for incident in incidents_list:
        if int(incident.record_id) == int(incident_id):
            incident.type = data['type']
            incident.id = data['id']
            incident.comment = data['comment']
            incident.location = data['location']
            incident.status = 200
            incident.images = data['Images']
            incident.videos = data['Videos']
            incident.createdBy = data['createdBy']
            incident.createdOn = data['createdOn']
    return jsonify({
        "status": 200,
        "message": "incident updated"
        }), 200


@app.route('/api/v1/incidents/<int:incident_id>', methods=['DELETE'])
def delete_record(incident_id):
    # deleting an incident
    if incident_id == 0 or incident_id > len(incidents_list):
        return jsonify({"message": "Index out of range"}), 400
    for incident in incidents_list:
        if incident.id == incident_id:
            incidents_list.remove(incident)
    return jsonify({
        "status": 200,
        "message": "deleted incident"
        }), 200

@app.route('/api/v1/users', methods=['POST'])
def create_user():
    # creating a user
    data = request.get_json()
    id = len(users)+1
    registered = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    isAdmin = False


    user = User(id, data['firstname'], data['lastname'],
                data['othernames'], data['email'], data['phoneNumber'],
                data['username'], registered, isAdmin)
    
    users.append(user)

    return jsonify({
        "message": "User created",
        "status": 201,
        "data": user
        }), 201

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    # getting all users
    user = [user.get_user_details() for user in users]
    return jsonify({
        "data": user
        }), 200


@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
# getting one user
def get_one_user(user_id):
    fetched_user = []
    user = users[user_id - 1]
    fetched_user.append(user.get_user_details())
    return jsonify({
        "data": fetched_user}
        ), 200


@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # deleting a user
    if user_id == 0 or user_id > len(users):
        return jsonify({"message": "Index out of range"}), 400
    for user in users:
        if user.id == user_id:
            users.remove(user)
    return jsonify({"message": "account successfully deleted"}), 200
