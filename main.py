import json

from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
from clase import Patient
from pacientes import load_patients

app = Flask(__name__)
patients_obj: list = load_patients()

if __name__ == "__main__":
    app.run(debug=True , port=5000)

#anda bien
@app.route("/api/patients", methods=['GET'])
def get_all_clients():
    return jsonify([patient.serialize() for patient in patients_obj])

#no funciona
@app.route("/api/patients/<client_id>", methods=['GET'])
def get_client(client_id):
    for patient in patients_obj:
        if patient.id == client_id:

            return jsonify(patient.serialize())

    return jsonify({})
@app.route("/api/patients/...", methods=['POST'])
def create_client():
    client = request.json

    try:
        new_client = Client(
            client_id_generator(),
            client['date_created'],
            client['first_name'],
            client['last_name'],
            client['date_created'],
            client['document'],
            client['gender'],
            client['phone_number'],
            client['email'],
            client['client_status'],
            ClientAddress(
                client['client_address']['street'],
                client['client_address']['street_number'],
                client['client_address']['city'],
                client['client_address']['state'],
                client['client_address']['post_code'],
                client['client_address']['country']
            )
        )

        clients.append(new_client)

    except KeyError as key_err:
        missing_param = (key_err.__str__())
        return jsonify(
            error_code="ERROR_BAD",
            error_description="Bad request",
            error_body=missing_param
        ), 400

    return jsonify(new_client.serialize())


@app.route("/api/digital-bank/client-test", methods=['POST'])
def creat_test_data():
    client = request.json
    client['id'] = client_id_generator()
    client['role'] = request.args['role']
    store_client_file(client)

    print(request.args['role'])

    # response = make_response(client, 201)
    # return response

    return client, 200
