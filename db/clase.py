# creacion de la clase paciente
class Patient:

    def __init__(self,  nombre, apellido, fecha_de_nacimiento, obra_social, codigo_postal, altura, alergias, id) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.obra_social: ObraSocial = obra_social
        self.codigo_postal = codigo_postal
        self.altura = altura
        self.alergias = alergias
        self.id = id

    def serialize(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'nacimiento': self.fecha_de_nacimiento,
            'obra_social': self.obra_social.serialize(),
            'codigo_postal': self.codigo_postal,
            'altura': self.altura,
            'alergias': self.alergias,
            'id': self.id,
        }

# creacion una clase hija para la obra social
class ObraSocial(Patient):

    def __init__(self, nombre, plan, numero_tarjeta) -> None:
        self.nombre = nombre
        self.plan = plan
        self.numero_tarjeta = numero_tarjeta


    def serialize(self):
        return {
            'nombre': self.nombre,
            'plan': self.plan,
            'numero_tarjeta': self.numero_tarjeta,
        }
