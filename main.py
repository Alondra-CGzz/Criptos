import os
from Modulos import datos_tratados_00 as data
from Modulos import mod_utiles as mod
from Modulos import consultas as info
from Modulos import estadisticas as cal

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
                      """, 9)         
                info.consultar_dato(monedas,coin, opcion1)

            elif opcion == 2:
                pass
            elif opcion == 3:
                opcion3 = mod.validar("""
             - Datos -             
                                                                       
        1) Promedio de precios entre las monedas 
        2) Rango en los precios de las monedas
        3) Recomendación de 5 monedas según el porcentaje de cambio cada semana 
                      
    Seleccione una opción: """, 3)   
                cal.calculos(opcion3)

            elif opcion == 4:
                opcion4 = mod.validar("""
             - Datos -             
                                                                       
        1) Porcentaje de cambio cada 24 horas
        5) Porcentaje de cambio cada 7 días
        6) Precio en btc
        7) Número de monedas que se han comercializado
        8) Suministro circulante
        9) Suministro máximo posible
                      
    Seleccione una opción: """, 9)  
                
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



