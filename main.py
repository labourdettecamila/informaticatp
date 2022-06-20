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

    
@app.route("/api/patients", methods=['GET'])
def get_all_clients():
    return jsonify([patient.serialize() for patient in patients_obj])


@app.route("/api/patients/<client_id>", methods=['GET'])
def get_client(client_id):
    for patient in patients_obj:
        if int(client_id) == patient.id::

            return jsonify(patient.serialize())

    return jsonify({})


@app.route("/api/<client_id>", methods=['PUT'])
def modify_patient(client_id):
    body = request.json

    contador = 0

    for patient in patients_obj:
        if patient.id == client_id:
            
            paciente_modificado = Patient(body["nombre"], body["apellido"], body["fecha_de_nacimiento"],
                                                          body["obra_social"], body["codigo_postal"], body["altura"],
                                                          body["alergias"], body["id"])
            
            patients_obj[contador:contador + 1] = paciente_modificado
            
            return jsonify(paciente_modificado.serialize())

        else:
            contador += 1
    return "No existe un paciente identificado con el ID: " + client_id



@app.route("/api/delete_patient/<client_id>", methods=['DELETE'])
def delete_patient(client_id):
    contador = 0

    for patient in patients_obj:
        if int(client_id) == patient.id:

            patients_obj[contador:contador+1] = []

            return "Paciente eliminado"
        else:
            contador += 1

    return "No existe un paciente identificado con el ID: " + client_id

@app.route("/api/add_patient", methods=['POST'])
def add_patient():
    patient = request.json

    try:
        new_patient = Patient(
            patient["nombre"],
            patient["apellido"],
            patient["nacimiento"],
            patient["obra_social"],
            patient["codigo_postal"],
            patient["altura"],
            patient["alergias"],
            patient["id"]
            )

        patients_obj.append(new_patient)

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


