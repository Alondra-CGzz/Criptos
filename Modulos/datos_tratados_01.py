import os, json
def acceder_json():
    ruta = os.getcwd()
    os.chdir(f"{ruta}\\ReportesDeConsultaApi")
    try: 
        with open("datos_de_monedas.json") as archivo: 
            datos = json.load(archivo)
        print(datos)

    except: 
        print("No hay información reciente")

acceder_json()