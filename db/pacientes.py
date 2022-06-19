from clase import Patient

pacientes_dic = [
    {
        "nombre": "Lara",
        "apellido": "Milberg",
        "fecha de nacimiento": "01/07/2003",
        "obra social": "osde",
        "codigo postal": "C1407AOM",
        "altura": 1.7, "peso": 60,
        "alergias": None,
        "id": 10025

    },
    {
        "nombre": "Lucas",
        "apellido": "Sanchez",
        "fecha de nacimiento": "27/11/2012",
        "obra social": "medicus",
        "codigo postal": "C1232AAC",
        "altura": 1.5, "peso": 47,
        "alergias": "acaros",
        "id": 10026

    },
    {
        "nombre": "Juana",
        "apellido": "Condomi",
        "fecha de nacimiento": "05/03/1984",
        "obra social": "osde",
        "codigo postal": "C1272AAA",
        "altura": 1.61, "peso": 73,
        "alergias": "hongos",
        "id": 10027

    },
     {
        "nombre": "Trinidad",
        "apellido": "Azpiri",
        "fecha de nacimiento": "07/04/2003",
        "obra social": "osde",
        "codigo postal": "C1407KQF",
        "altura": 1.59, "peso": 53,
        "alergias": "penicilina",
        "id": 10028

    },
     {
        "nombre": "Clara",
        "apellido": "Pinasco",
        "fecha de nacimiento": "12/02/2002",
        "obra social": "medicus",
        "codigo postal": "C1427ARN",
        "altura": 1.7, "peso": 56,
        "alergias": None,
        "id": 10029

    },
     {
        "nombre": "Martina",
        "apellido": "Larrea",
        "fecha de nacimiento": "11/11/2012",
        "obra social": "swiss medical",
        "codigo postal": "C1439CNU",
        "altura": 1.55, "peso": 60,
        "alergias": "alergia al polen",
        "id": 10030

    },
     {
        "nombre": "Felipe",
        "apellido": "Canale",
        "fecha de nacimiento": "31/08/2000",
        "obra social": "swiss medical",
        "codigo postal": "C1284AGA",
        "altura": 1.7, "peso": 87,
        "alergias": "acaros",
        "id": 10031

    }
]


def load_patients():
    patients_obj = []

    for patient in pacientes_dic:
        patients_obj.append(
                Patient(
                    patient['nombre'],
                    patient['apellido'],
                    patient['fecha de nacimiento'],
                    patient['obra social'],
                    patient['codigo postal'],
                    patient['altura'],
                    patient['alergias'],
                    patient['id']
                )
            )
    return patients_obj

pacientes_objetos = load_patients()

