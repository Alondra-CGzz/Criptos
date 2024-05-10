import os, json, openpyxl 
import pandas as pd


def archivo(lista,ruta, nombre):
    os.chdir(f"{ruta}\\ReportesDeConsultaApi")
    archivo = pd.read_excel("datos_de_monedas.xlsx", usecols= lista)

    os.chdir(f"{ruta}\\ReportesDeDatosNuméricos")
    #creamos el archivo en excel con solo los datos de sc, sm y name
    archivo.to_excel(f"{nombre}.xlsx", index= False, header = True)#header para q aparezcan los subtemas e index para q no aparezcan numerados los datos

    archive = openpyxl.load_workbook(f"{nombre}.xlsx")
    hoja = archive.active
    return hoja, archive

def estadisticas(total, opcion,ruta):
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
        lista = [2,5] 
        hoja, archive = archivo(lista,ruta ,"porcent_cambio")

        for i in range(2, total):
            nombre = hoja[f"A{i}"].value
            por = hoja[f"B{i}"].value

            if por>0:
                hoja[f"C{i}"] = nombre
                hoja[f"D{i}"] = por
                print(f"{nombre} - {por}%")
        
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
