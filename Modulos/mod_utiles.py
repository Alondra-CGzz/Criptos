
def validar(msj):
    while True:
        try: 
            valor = int(input(msj))
            if valor<0:
                print("Ingrese un valor númerico valido")
            else:
                break
        except ValueError: 
            print("Ingrese un valor númerico valido")
            continue
    return valor
