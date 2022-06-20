import json

from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
from clase import Patient, ObraSocial
from pacientes import load_patients

app = Flask(__name__)
patients_obj: list = load_patients()

if __name__ == "__main__":
    app.run(debug=True , port=5000)

    
@app.route("/api/patients", methods=['GET'])
def get_all_clients():
    return jsonify([patient.serialize() for patient in patients_obj])


@app.route("/api/patients/<paciente_id>", methods=['GET'])
def get_client(paciente_id):
    for patient in patients_obj:
        if int(paciente_id) == patient.id:
            return jsonify(patient.serialize())
    return [{}]


@app.route("/api/hospitales/<paciente_id>", methods=['GET'])
def get_hospital(paciente_id):

        for patient in patients_obj:
            if int(paciente_id) == patient.id:
                for hospi in hospitales:
                    if hospi["cod_postal"] == patient.codigo_postal:
                        return hospi
            else :
                return jsonify(
                    error_code="ERROR_BAD",
                    error_description="Bad request",
                    error_body=" no existe el paciente"
                    ), 500

            
@app.route("/api/modify", methods=['PUT'])
def modify_patient():
    body = request.get_json()
    id_buscado = body["id"]

    contador = 0

    for patient in patients_obj:
        if patient.id == int(id_buscado):

            paciente_modificado = Patient(body["nombre"],
                                          body["apellido"],
                                          body["nacimiento"],
                                          ObraSocial(body["obra_social"]["nombre"], body["obra_social"]["plan"],
                                                     body["obra_social"]["numero_tarjeta"]),
                                          body["codigo_postal"],
                                          body["altura"],
                                          body["peso"],
                                          body["alergias"],
                                          body["id"])

            patients_obj[contador] = paciente_modificado

            return jsonify(paciente_modificado.serialize())

        else:
            contador += 1
    return "No existe un paciente identificado con el ID: " + id_buscado


@app.route("/api/delete_patient/<client_id>", methods=['DELETE'])
def delete_patient(client_id):
    contador = 0

    for patient in patients_obj:
        if int(client_id) == patient.id:

            patients_obj[contador] = []

            return "Paciente eliminado"
        else:
            contador += 1

    return "No existe un paciente identificado con el ID: " + client_id


@app.route("/api/add_patient1", methods=['POST'])
def add_patient1():

    patient = request.get_json()

    try:
        new_patient = Patient(
            patient["nombre"],
            patient["apellido"],
            patient["nacimiento"],
            ObraSocial(patient["obra_social"]["nombre"], patient["obra_social"]["plan"], patient["obra_social"]["numero_tarjeta"]),
            patient["codigo_postal"],
            patient["altura"],
            patient["peso"],
            patient["alergias"],
            patient["id"])

        patients_obj.append(new_patient)


    except KeyError as key_err:
        missing_param = (key_err.__str__())
        return jsonify(
            error_code="ERROR_BAD",
            error_description="Bad request",
            error_body=missing_param
        ), 400

    return jsonify(new_patient.serialize())
