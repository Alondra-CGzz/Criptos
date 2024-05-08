import requests, json, os
from openpyxl import Workbook
from Modulos import mod_utiles as mod

def request(limite):
    url = "https://api.coinlore.net/api/tickers/" 
    response = requests.get(f"{url}?start=0&limit={limite}")

    if response.status_code == 200:
        archivo = json.loads(response.text)
        datos = archivo.get("data", [])
        return datos


def crear_json_coins(limite):
    datos = request(limite)

    #eliminar lo que no se usara
    for i in datos:
        del i["volume24"]
        del i["nameid"]
        del i["price_usd"]
        del i["market_cap_usd"]
        del i["tsupply"]
        del i["percent_change_1h"]

    #guardar el archivo
    #cambiamos a la ruta de consulta api  
    ruta = os.getcwd()
    os.chdir(f"{ruta}\\ReportesDeConsultaApi")

    #crear el json de las monedas que aparecieron ante el usuario
    with open("datos_de_monedas.json", "w") as archivo: 
        json.dump(datos, archivo, indent = 3)
    os.chdir(ruta)


def crear_xlsx_coins(limite):
    datos = request(limite)

    book = Workbook()
    sheet = book.active
    #subtema
    lista = [ "Id", "Simbología", "Name", "Rank", "Porcentaje cada 24 horas", "Porcentaje cada 7 días", "Precio en btc", "Coins comercializadas", "Suministro circulante", "Suministro máximo"]
    sheet.append(lista)
    
    #los datos
    cont = 2
    for i in datos: 
        sheet[f"A{cont}"] = i["id"]
        sheet[f"B{cont}"] = i["symbol"]
        sheet[f"C{cont}"] = i["name"]
        sheet[f"D{cont}"] = i["rank"] 
        sheet[f"E{cont}"] = i["percent_change_24h"]
        sheet[f"F{cont}"] = i["percent_change_7d"] 
        sheet[f"G{cont}"] = i["price_btc"]
        sheet[f"H{cont}"] = i["volume24a"] 
        sheet[f"I{cont}"] = i["csupply"]
        sheet[f"J{cont}"] = i["msupply"]
        cont += 1

    #guardar el archivo
    ruta = os.getcwd()
    os.chdir(f"{ruta}\\ReportesDeConsultaApi")
    book.save("datos_de_monedas.xlsx")
    os.chdir(ruta)
    
def dato(lista):
    total = len(lista)
    while True: 
        try: 
            moneda = int(input("Ingrese el número de la moneda que desea buscar: "))
            if moneda<0 or moneda>total:
                print("Ingrese un valor númerico valido")
            else:
                break

        except ValueError: 
            print("Ingrese un valor númerico valido")    
    return moneda

def liste(datos, lista, cont):
    for coin in datos:
        nom = coin["name"]
        lista.append(nom)
        print(f"{cont}-{nom}")
        cont += 1
    total = cont
    return lista, total

def coins(cont,lista, start = 0, url = "https://api.coinlore.net/api/tickers/"):  
    """Por si acaso el limite lo queremos de 11 datos lo marcare con #"""
    response = requests.get(f"{url}?start={start}&limit=11")#

    if response.status_code == 200:
        archivo = json.loads(response.text)
        datos = archivo.get("data", [])

        #limite de las monedas que se trataran
        if datos != []:
            print("\n\t**Lista de coins ha tratar**\n")
            lista, cont = liste(datos, lista, cont)
        
        
        continuar = mod.validar("\n¿Desea continuar listando? \t1-Si \t2-No\n",2)
        if continuar == 1:
            coins(cont, lista, start= start+11)

        return lista
