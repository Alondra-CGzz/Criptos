#funcion del cambio de ruta
#hacer menu con un array
import os


def validar(msj, lim):
    while True:
        try: 
            valor = int(input(msj))
            if valor<=0 or valor>lim:
                print("Ingrese un valor dentro del rango")
            else:
                break
        except ValueError: 
            print("Ingrese un valor númerico valido")
            continue
    return valor

def crear_dir():
    ruta = os.getcwd()
    try: 
        os.chdir(f"{ruta}\\ReportesDeConsultaApi")
    except:
        os.makedirs(f"{ruta}\\ReportesDeConsultaApi")
        os.makedirs(f"{ruta}\\ReportesDeDatosNuméricos")
    os.chdir(ruta)

