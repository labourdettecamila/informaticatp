import json
from pacientes_class import Patient

def load_patients():
    patients = []

    with open('pacientes.py', 'r') as file:
        patients_json = json.load(file)
        for patient in patients_json:
            patients.append(
                Patient(
                    patient['nombre'],
                    patient['apellido'],
                    patient['fecha_de_nacimiento'],
                    patient['obra_social'],
                    patient['codigo_postal'],
                    patient['altura'],
                    patient['alergias'],
                    patient['id']
                )
            )
    return patients


