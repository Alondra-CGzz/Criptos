import os, json, openpyxl 
import pandas as pd
ruta = os.getcwd()
os.chdir(f"{ruta}\\ReportesDeConsultaApi")

def estadisticas(total, opcion):
    if opcion == 1:
        pass
    elif opcion == 2:
        pass
    elif opcion == 3:
        lista = [2,8,9] #es segun el indice de las columnas en los datos de las monedas
        archivo = pd.read_excel("datos_de_monedas.xlsx", usecols= lista)
        os.chdir(f"{ruta}\\ReportesDeDatosNuméricos")
        #creamos el archivo en excel con solo los datos de sc, sm y name
        archivo.to_excel("porcentajes.xlsx", index= False, header = True)#header para q aparezcan los subtemas e index para q no aparezcan numerados los datos

        archive = openpyxl.load_workbook("porcentajes.xlsx")
        hoja = archive.active
        hoja["D1"] = "Division"
        hoja["E1"] = "Porcentaje"

        for i in range(2, total+2):
            sc = hoja[f"B{i}"].value
            sm = hoja[f"C{i}"].value
            try: 
                hoja[f"D{i}"] = sc/sm  
            except:
                hoja[f"D{i}"] = "n"

        print("El porcentaje de suministro con respecto al limite existente de...")
        for i in range(2, total+2):
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
    else:
        pass

    os.chdir(ruta)

estadisticas(22, 3)