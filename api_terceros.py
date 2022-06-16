import requests
url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/salud/hospitales/hospitales.geojson'

response = requests.get(url)

hospitales_api = (response.json())

#rint(hospitales_api["features"][0]["properties"]  )

hospitales = []

for hospital in hospitales_api["features"][0]["properties"]:

      hosp = {"nombre" : hospital["NOMBRE"],
              "calle" : hospital["CALLE"],
              "altura" : hospital["ALTURA"],
              "cod_postal" : hospital["COD_POSTAL"]}
      hospitales.append(hosp)

print(hospitales)

nombre = hos

