#funcion del cambio de ruta
#hacer menu con un array


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
