import os
from Modulos import datos_tratados_00 as data
from Modulos import mod_utiles as mod
from Modulos import consultas as info


def limpiar():
    os.system("cls")

if __name__ == '__main__':

    #menu
    while True:
        try: 
            opcion = int(input("""
            - MENÚ -
                            
        1) Consultas web
        2) Consultas de registros
        3) Estadísticas
        4) Gráficas     
        5) Borrar todo  
        6) Salir
            
    Seleccione una opción: """))

            if opcion == 1:
                monedas, coin = data.coins(0, [])
                data.crear_json_coins(len(monedas))
                data.crear_xlsx_coins(len(monedas))
                print(monedas, coin)

                #submenu
                opcion1 = mod.validar("""
    - Información posible a consultar -                  
        1) Id
        2) Simbología
        3) Rank
        4) Porcentaje de cambio cada 24 horas
        5) Porcentaje de cambio cada 7 días
        6) Precio en btc
        7) Número de monedas que se han comercializado
        8) Suministro circulante
        9) Suministro máximo posible
                      """)         
                info.consultar_dato(monedas,coin, opcion1)
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                limpiar()
                print("""
    - Información disponible para gráficas -                  
        1) Porcentaje de cambio cada 24 horas
        5) Porcentaje de cambio cada 7 días
        6) Precio en btc
        7) Número de monedas que se han comercializado
        8) Suministro circulante
        9) Suministro máximo posible
                      """)
            elif opcion == 5:
                pass
            elif opcion == 6:
                limpiar()
                print("Que tenga un bonito día! =)")
                break
            else: 
                limpiar()
                print("\n***Ingrese una opción válida***")
                continue 

        except ValueError:
            limpiar()
            print("\n***Ingrese un valor númerico válido***")
            continue




"""
1. Consultas web – Se podrán hacer consultas en tiempo real a la API, el equipo deberá diseñar el submenú para que el usuario sea guiado sobre 
qué datos puede consultar. Al finalizar la consulta la información guardada se almacena en las estructuras de datos o, de ser necesario, en 
los archivos correspondientes.

2. Consultas de registros – El usuario podrá consultar información cuando no se encuentre conectado a Internet

3. Estadísticas – Se espera que parte de los datos obtenidos por la API sean numéricos o puedan generar colecciones de datos o similares que
permitan tener datos cuantitativos. Por ejemplo, pueden usar la API de maquillaje y consular los precios promedio o pueden consultar la API 
de Star Wars y ellos mismos construir sus datos de cuántos personajes con determinado color de cabello hay, y de ahí sacar los porcentajes
de personajes con cabello negro, rubio, etc. Este menú permitirá recalcular y ver en pantalla las estadísticas obtenidas.

4. Gráficas – Se debe generar un menú para desplegar al menos 3 gráficas diferentes.

5. Borrar todo – Se tendrá la opción de eliminar todos los registros de la aplicación – Es necesario que el estudiante investigue como 
eliminar."""