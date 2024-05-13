import os, json, openpyxl 
import pandas as pd

def partir(L, bajo, alto, l):
    pivote = L[alto]
    i = bajo -1

    for j in range(bajo, alto):
        if L[j] <= pivote:
            i += 1
            l[i], l[j] = l[j], l[i]
            L[i], L[j] = L[j], L[i]
    L[i+1], L[alto] = L[alto] , L[i+1]
    
    l[i+1], l[alto] = l[alto], l[i+1]
    return i+1

def quicksort(L, bajo, alto, l):
    if bajo<alto:
        p = partir(L, bajo, alto, l)
        quicksort(L, bajo, p-1, l)
        quicksort(L, p+1, alto, l)


def archivo(lista,ruta, nombre):
    os.chdir(f"{ruta}\\ReportesDeConsultaApi")
    archivo = pd.read_excel("datos_de_monedas.xlsx", usecols= lista)

    os.chdir(f"{ruta}\\ReportesDeDatosNuméricos")
    #creamos el archivo en excel con solo los datos de sc, sm y name
    archivo.to_excel(f"{nombre}.xlsx", index= False, header = True)#header para q aparezcan los subtemas e index para q no aparezcan numerados los datos

    archive = openpyxl.load_workbook(f"{nombre}.xlsx")
    hoja = archive.active
    return hoja, archive

def estadisticas(total, opcion, ruta):
    total = total + 2

    if opcion == 1:
        lista = [2,6] 
        hoja, archive = archivo(lista,ruta ,"precios")

        hoja["D2"] = "Max"
        hoja["E2"] = "Min"

        hoja["D3"] = f"=MAX(B2:B{total})"
        hoja["E3"] = f"=MIN(B2:B{total})"
        max = hoja["D3"].value
        min = hoja["E3"].value

        print(f"Los precios varian de {min}-{max} ")
        archive.save("precios.xlsx")

    elif opcion == 2:
        nombre = []
        por = []
        os.chdir(f"{ruta}\\ReportesDeConsultaApi")
        with open("datos_de_monedas.json") as data:
           datas = json.load(data)
        for i in datas:
            por.append(i["percent_change_7d"])
            nombre.append(i["name"])
        data.close() #cerramos el json

        quicksort(por, 0, len(por)-1, nombre) #metodo de ordenamiento

        print(por, nombre)
          
        #archivo excel
        lista = [2,5] 
        hoja, archive = archivo(lista,ruta ,"porcent_cambio")

        cont = 0
        #cuando ya este orddenado segun el metodo quicksort
        for i in range(2, total):   
            name = nombre[cont]     
            porcent = por[cont] 

            hoja[f"C{i}"] = name
            hoja[f"D{i}"] = porcent
            print(f"{name} - {porcent}%")
            cont += 1

        archive.save("porcent_cambio.xlsx")
        


    elif opcion == 3:
        lista = [2,8,9] 
        hoja, archive = archivo(lista,ruta, "porcent_suministro")

        hoja["D1"] = "Division"
        hoja["E1"] = "Porcentaje"

        for i in range(2, total):
            sc = hoja[f"B{i}"].value
            sm = hoja[f"C{i}"].value
            try: 
                hoja[f"D{i}"] = sc/sm  
            except: 
                hoja[f"D{i}"] = "n"

        print("El porcentaje de suministro con respecto al limite existente de...")
        for i in range(2, total):
            num = hoja[f"D{i}"].value
            moneda = hoja[f"A{i}"].value

            if num == "n":
                hoja[f"E{i}"] = "Sin limite"
                print(f"\"{moneda}\" no cuenta con un limite")
            else: 
                valor = round(num*100) #lo queremos redondeado al entero mas cercano 
                hoja[f"E{i}"] = valor
                print(f"\"{moneda}\" es {valor}%")

        archive.save("porcentajes.xlsx")

    os.chdir(ruta)
