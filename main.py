import json

from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
from clase import Patient, ObraSocial
from pacientes import load_patients
from api import hospitales

app = Flask(__name__)
patients_obj: list = load_patients()

if __name__ == "__main__":
    app.run(debug=True , port=5000)


# obtiene toda la lista de clientes    
@app.route("/api/patients", methods=['GET'])
def get_all_clients():
    return jsonify([patient.serialize() for patient in patients_obj])


# obtiene cliente segun id
@app.route("/api/patients/<paciente_id>", methods=['GET'])
def get_client(paciente_id):
    
    # recorre la lista de pacientes actuales
    for patient in patients_obj:
        
        # comparo el id del paciente que estoy recorriendo con el id que paso como parametro
        if int(paciente_id) == patient.id:
            return jsonify(patient.serialize())
    return [{}]


# obtiene hospitales mas cercanos segun id
@app.route("/api/hospitales/<paciente_id>", methods=['GET'])
def get_hospital(paciente_id):
    
        # recorre la lista de pacientes actuales
        for patient in patients_obj:
            
            # comparo el id del paciente que estoy recorriendo con el id que paso como parametro
            if int(paciente_id) == patient.id:
                
                # recorro la lista de hospitales
                for hospi in hospitales:
                    
                    # si el codigo postal del hospital que estoy recorriendo coincide con el codigo postal del paciente, devuelve el hospital
                    if hospi["cod_postal"] == patient.codigo_postal:
                        return jsonify(hospi)
            else :
                return jsonify(
                    error_code="ERROR_BAD",
                    error_description="Bad request",
                    error_body=" no existe el paciente"
                    ), 500


# modificar un paciente existente            
@app.route("/api/modify", methods=['PUT'])
def modify_patient():
    
    # asigno a la variable body el diccionario que ingrese por postman
    body = request.get_json()
    id_buscado = body["id"]

    contador = 0

    # recorre la lista de pacientes actuales
    for patient in patients_obj:
        
        # comparo el id del paciente que estoy recorriendo con el id del paciente que ingrese en postman
        if patient.id == int(id_buscado):
            
            # si los ids coinciden, creo un nuevo objeto con los atributos ingresados en postman
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
            
            # asigno el paciente modificado en el lugar donde estaba anteriormente
            patients_obj[contador] = paciente_modificado

            return jsonify(paciente_modificado.serialize())

        else:
            
            # si los ids no coinciden sumo uno al contador
            contador += 1
            
    # si el id del paciente ingresado en postman no existe devuelve:        
    return "No existe un paciente identificado con el ID: " + id_buscado


@app.route("/api/delete_patient/<client_id>", methods=['DELETE'])
def delete_patient(client_id):
    contador = 0
    
    # recorre la lista de pacientes actuales
    for patient in patients_obj:
        
        # comparo el id del paciente que estoy recorriendo con el id del paciente que quiero eliminar
        if int(client_id) == patient.id:
            
            # si los ids coinciden elimino el paciente
            patients_obj[contador] = []

            return "Paciente eliminado"
        else:
            
            # si los ids no coinciden le sumo 1 al contador
            contador += 1

    # si el id del paciente ingresado en postman no existe devuelve:           
    return "No existe un paciente identificado con el ID: " + client_id


# crear nuevo paciente
@app.route("/api/add_patient1", methods=['POST'])
def add_patient1():

    # creo una variable que guarda los datos del nuevo cliente ingresados en postman
    patient = request.get_json()

    try:
        
        # con los datos del nuevo paciente creo un objeto 
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

        # agrego el nuevo paciente a la lista 
        patients_obj.append(new_patient)


    except KeyError as key_err:
        missing_param = (key_err.__str__())
        return jsonify(
            error_code="ERROR_BAD",
            error_description="Bad request",
            error_body=missing_param
        ), 400

    return jsonify(new_patient.serialize())
