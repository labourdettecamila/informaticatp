import random


def patient_id_generator():
    return str(random.randint(1000000, 9000000))


class Patient:

    def __init__(self,  nombre, apellido, fecha_de_nacimiento, obra_social, codigo_postal, altura, alergias, id) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.obra_social = obra_social
        self.codigo_postal = codigo_postal
        self.altura = altura
        self.alergias = alergias
        self.id = id

    def serialize(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'nacimiento': self.fecha_de_nacimiento,
            'obra_social': self.obra_social,
            'codigo_postal': self.codigo_postal,
            'altura': self.altura,
            'alergias': self.alergias,
            'id': self.id,
        }
