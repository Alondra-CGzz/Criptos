import os, shutil
from Modulos import mod_utiles as mod
from Modulos import consultas as info
from Modulos import estadisticas as cal
from Modulos import datos_tratados_00 as data
from Modulos import datos_tratados_01 as data_descargada
from Modulos import graficas as gf
ruta_dir_padre= os.path.dirname(os.path.abspath(__file__))
os.chdir(ruta_dir_padre)

def limpiar():
    os.system("cls")

if __name__ == '__main__':
    print("""
         **** ACCESO A LA INFORMACIÓN DE CRIPTOMONEDAS ****""")
    x = True
    
    try:
        monedas = data.coins(0, [])
        data.crear_json_coins(len(monedas), ruta_dir_padre)
        data.crear_xlsx_coins(len(monedas), ruta_dir_padre)
    except:
        limpiar()
        print("\n\tLo sentimos, no es posible consumir la api, sin embargo accederemos a los ultimos registros\n")
        data_descargada.acceder_json(ruta_dir_padre)
        x = False


    #menu
    while x:
        mod.crear_dir(ruta_dir_padre) #crea las carpetas
        
        try: 
            opcion = int(input("""       

            - Menú -
                            
        1) Consultas web
        2) Consultas de registros
        3) Estadísticas
        4) Gráficas     
        5) Borrar todo  
        6) Salir
            
    Seleccione una opción: """))


            if opcion == 1:
                print("\n\t -- Actualización de datos --\n")
                monedas = data.coins(0, [])
                data.crear_json_coins(len(monedas), ruta_dir_padre)
                data.crear_xlsx_coins(len(monedas), ruta_dir_padre)
                coin = data.dato(monedas)

                opcion1 = mod.validar("""
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
                info.consultar_dato(monedas,coin, opcion1, ruta_dir_padre)

            elif opcion == 2:  
                data_descargada.acceder_json(ruta_dir_padre)

            elif opcion == 3:
                opcion3 = mod.validar("""
             - Datos -             
                                                                       
        1) Rango en los precios de las monedas
        2) Recomendación de 5 monedas según el porcentaje de cambio cada semana 
        3) Porcentajes según el suministro de monedas actual
                      
    Seleccione una opción: """, 3)   
                try:
                    cal.estadisticas(len(monedas), opcion3, ruta_dir_padre)
                except:
                    print("\nNo existe información reciente")

            elif opcion == 4:
                opcion4 = mod.validar("""
             - Datos -             
                                                                       
        1) Porcentaje de cambio cada 7 días
        2) Precio en btc
        3) Monedas comercializadas
                      
    Seleccione una opción: """, 3)  
                gf.grafica(monedas, ruta_dir_padre, opcion4)
                
            elif opcion == 5:
                print("\n\tTodo se borro satisfactoriamente\n")
                shutil.rmtree(f"{ruta_dir_padre}\\Gráficas")
                shutil.rmtree(f"{ruta_dir_padre}\\ReportesDeConsultaApi")
                shutil.rmtree(f"{ruta_dir_padre}\\ReportesDeDatosNuméricos")



            elif opcion == 6:
                limpiar()
                print("Que tenga un bonito día! =)")
                break
            else: 
                limpiar()
                print("\n***Ingrese una opción válida***")
                continue 

        except:
            limpiar()
            print("\n***Ingrese un valor númerico válido***")
            continue

