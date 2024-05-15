import json, os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def g_1(ruta):
    os.chdir(f"{ruta}\\ReportesDeConsultaApi")
    with open("datos_de_monedas.json") as data:
        datas = json.load(data) 

    cambio7 =  []
    simbolos = []
    for i in datas:
        num = float(i["percent_change_7d"])
        cambio7.append(num)

        simbolos.append(i["symbol"])
    data.close()
        
    x = np.array(simbolos)
    y = np.array(cambio7)
    plt.title("*PORCENTAJE DE CAMBIO CADA 7 DIAS*", color='red') 
    plt.xlabel("Monedas", color='blue') 
    plt.ylabel("Porcentaje", color='blue') 
    plt.bar(x,y, width =0.5, color='yellow')
    nombre = "porcentaje_7d"
    os.chdir(f"{ruta}\\Gráficas")
    plt.savefig(f"grafica_{nombre}.jpg")
    plt.show()

def g_2(ruta):
    os.chdir(f"{ruta}\\ReportesDeConsultaApi")
    datos = pd.read_excel("datos_de_monedas.xlsx")
    df = pd.DataFrame(datos)
    df.groupby("Name")["Precio en btc"].median().plot(kind = "barh", legend="reverse")
    plt.xlabel("Precio en btc")
    nombre = "precio"
    os.chdir(f"{ruta}\\Gráficas")
    plt.savefig(f"grafica_{nombre}.png")
    plt.show()

def g_3(ruta):
    os.chdir(f"{ruta}\\ReportesDeConsultaApi")
    datos = pd.read_excel("datos_de_monedas.xlsx")
    df = pd.DataFrame(datos)
    df.groupby("Simbología")["Coins comercializadas"].sum().plot(kind="pie",colormap="Paired")
    plt.axis("equal")
    nombre = "comercio"
    os.chdir(f"{ruta}\\Gráficas")
    plt.savefig(f"grafica_{nombre}.jpg")
    plt.show()



def grafica(lista_monedas, ruta, opcion):
    if opcion == 1:
       g_1(ruta)

    elif opcion == 2:
        g_2(ruta)
        
    elif opcion == 3:
        g_3(ruta)
        


            


