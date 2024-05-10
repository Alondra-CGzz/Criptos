import os, json
def consultar_dato(lista_monedas,index_moneda, opcion_menu, ruta):
    os.chdir(f"{ruta}\\ReportesDeConsultaApi")

    #abrimos el archivo 
    with open("datos_de_monedas.json") as archivo:
        datos = json.load(archivo)

    
    opciones = ["id","symbol","rank","percent_change_24h","percent_change_7d","price_btc","volume24a","csupply","msupply"]
    opciones_nombre = [ "Id", "Simbología", "Rank", "Porcentaje cada 24 horas", "Porcentaje cada 7 días", "Precio en btc", "Coins comercializadas", "Suministro circulante", "Suministro máximo"]

    opcion_menu = opcion_menu - 1
    index_opcion = opciones[opcion_menu]
    print(f"""
        *{lista_monedas[index_moneda].upper()}*
    {opciones_nombre[opcion_menu]}: {datos[index_moneda][index_opcion]}\n""")

    os.chdir(ruta)