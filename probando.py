import random

def patient_id_generator():
    return (random.randint(1000000, 9000000))

class Patient:

    def __init__(self, id, nombre, apellido, fecha_de_nacimiento, obra_social, medico, codigo_postal, altura, peso, alergias) -> None:
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.obra_social = obra_social
        self.medico = medico
        self.codigo_postal = codigo_postal
        self.altura = altura
        self.peso = peso
        self.alergias = alergias

    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'fecha_de_nacimiento': self.fecha_de_nacimiento,
            'obra_social': self.obra_social,
            'medico': self.medico,
            'codigo_postal': self.codigo_postal,
            'altura': self.altura,
            'peso': self.peso,
            'alergias': self.alergias,
        }

example = Patient(patient_id_generator(), "Camila", "Labourdette", "24/03/03", "Osde 310", "José Luis Etchepare", "1424", 1.60, 56, "Acaros")
example_2 = Patient(patient_id_generator(), "Lara", "Milberg", "01/07/2003", "Osde","José Luis Etchepare", "C1407AOM", 1.7, 60, None)
example_3 = Patient(patient_id_generator(), "Lucas", "Sánchez", "27/11/2012", "Medicus", "Claudia Gomez Suarez", "C1232AAC", 1.5, 47, "Acaros")

def historia_clinica(self):
    return f"Historia clínica del paciente {self.id}:" \
           f"\n\tNombre: {self.nombre}" \
           f"\n\tApellido: {self.apellido}" \
           f"\n\tFecha de nacimiento: {self.fecha_de_nacimiento}" \
           f"\n\tObra social: {self.obra_social}" \
           f"\n\tMedico: {self.medico}" \
           f"\n\tCódigo postal: {self.codigo_postal}" \
           f"\n\tAltura: {self.altura}" \
           f"\n\tPeso: {self.peso}" \
           f"\n\tAlergias: {self.alergias}"

print(historia_clinica(example))

print("\n")

pacientes_list = [example, example_2, example_3]

import json
example_json = json.dumps(example.__dict__)
print("\n")
print(example_json)

pacientes_json = []
for patient in pacientes_list:
    pacientes_json.append(json.dumps(patient.__dict__))
print(pacientes_json)

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def saludo():
    return jsonify({'message': 'Api médica!'})

@app.route("/pacientes", methods=['GET'])
def get_pacientes():
    return jsonify([i.serialize() for i in pacientes_list])


if __name__ == "__main__":
    app.run(debug=True, port=6000)


