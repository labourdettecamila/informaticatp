import requests
url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/salud/hospitales/hospitales.geojson'


# guardo en la variable response la informacion de la url
response = requests.get(url)

hospitales_api = (response.json())

# creo una lista de hospitales 
hospitales = []

# recorro la lista de hospitales
for hospital in hospitales_api["features"]:
    
    # creo un diccionario con la informacion relevante del hospital que estoy recorriendo
    hosp = {"nombre": hospital['properties']["NOMBRE"],
            "calle": hospital['properties']["CALLE"],
            "altura": hospital['properties']["ALTURA"],
            "cod_postal": hospital['properties']["COD_POSTAL"]}
    
    # agrego el diccionario a la nueva lista de hospitales
    hospitales.append(hosp)




