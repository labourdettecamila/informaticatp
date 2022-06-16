import requests
url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/salud/hospitales/hospitales.geojson'

response = requests.get(url)

hospitales_api = (response.json())

#print(hospitales_api["features"][1]["properties"])

hospitales = []

for hospital in hospitales_api["features"]:
    hosp = {"nombre": hospital['properties']["NOMBRE"],
            "calle": hospital['properties']["CALLE"],
            "altura": hospital['properties']["ALTURA"],
            "cod_postal": hospital['properties']["COD_POSTAL"]}
    hospitales.append(hosp)

print(hospitales)




