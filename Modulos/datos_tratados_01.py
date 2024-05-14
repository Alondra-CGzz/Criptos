import os, json
from Modulos import datos_tratados_00 as data
from Modulos import consultas as consulta
from Modulos import mod_utiles as mod

def acceder_json(ruta):
    os.chdir(f"{ruta}\\ReportesDeConsultaApi")
    
    try: 
        with open("datos_de_monedas.json") as archivo: 
            datos = json.load(archivo)
        monedas, total_monedas = data.liste(datos, [], 0)
        coin = data.dato(monedas)
        os.chdir(ruta)
        opcion2 = mod.validar("""
                              
    - Información posible a consultar -      
                                                  
        1) Id
        2) Nombre
        3) Rank
        4) Porcentaje de cambio cada 24 horas
        5) Porcentaje de cambio cada 7 días
        6) Precio en btc
        7) Número de monedas que se han comercializado
        8) Suministro circulante
        9) Suministro máximo posible
                      """, 9)   
        
        consulta.consultar_dato(monedas, coin, opcion2, ruta)

    except FileNotFoundError: 
        print("\nNo hay información reciente")
    os.chdir(ruta) #porque habiamos cambiado de ruta y volvemos a la del directorio Pia
    

