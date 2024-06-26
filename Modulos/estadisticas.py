import os, json, openpyxl 
import pandas as pd
import numpy as np
from Modulos import datos_tratados_00 as modu

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

def estadisticas(opcion, ruta):
    os.chdir(f"{ruta}\\ReportesDeConsultaApi")
    with open("datos_de_monedas.json") as arch: 
            datos = json.load(arch)
    monedas = modu.tot_mon(datos)
    total_monedas= len(monedas)
    total = total_monedas + 2
    arch.close()

    if opcion == 1:
        lista = [2,6] 
        hoja, archive = archivo(lista,ruta ,"precios")

        hoja["D2"] = "Max"
        hoja["E2"] = "Min"

        #formulas de excel
        hoja["D3"] = f"=MAX(B2:B{total})"
        hoja["E3"] = f"=MIN(B2:B{total})"
        archive.save("precios.xlsx")
        
        os.chdir(f"{ruta}\\ReportesDeConsultaApi")
        with open("datos_de_monedas.json") as data:
           datas = json.load(data)

        mon =  []
        for i in datas:
            num = float(i["price_btc"])
            mon.append(num)
        data.close()
        
        maxi = max(mon)
        mini = min(mon)
        

        print(f"\n\tLos precios varian de ${mini} a ${maxi}")


    elif opcion == 2:
        nombre = []
        por = []
        os.chdir(f"{ruta}\\ReportesDeConsultaApi")
        with open("datos_de_monedas.json") as data:
           datas = json.load(data)
        for i in datas:
            num = float(i["percent_change_7d"])
            por.append(num)
            nombre.append(i["name"])
        data.close() #cerramos el json

        quicksort(por, 0, len(por)-1, nombre) #metodo de ordenamiento

        #archivo excel
        lista = [2,5] 
        hoja, archive = archivo(lista,ruta ,"porcent_cambio")
        hoja["C1"] = "Moneda"
        hoja["D1"] = "Porcentaje ordenado"

        cont = 0
        #cuando ya este orddenado segun el metodo quicksort
        for i in range(2, total):   
            name = nombre[cont]     
            porcent = por[cont] 

            hoja[f"C{i}"] = name
            hoja[f"D{i}"] = porcent
            cont += 1

        archive.save("porcent_cambio.xlsx")
        
        #Lista de recomendacion
        def closest(lst, K):   
            lst = np.asarray(lst)
            idx = (np.abs(lst - K)).argmin()
            return lst[idx]
        
        #hay q eliminar el elemento de ambas listas
        print("""
            Según su porcentaje de cambio cada 24 hrs los 5 mejores son:""")
        for i in range(0,5): 
            num = closest(por, 0)
            indice = por.index(num)

            name = nombre[indice]
            porcent = por[indice]
            print(f"\t{name} - {porcent}%")
            nombre.remove(name)
            por.remove(porcent)
          

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

        archive.save("porcentajes_suministro.xlsx")

    os.chdir(ruta)
