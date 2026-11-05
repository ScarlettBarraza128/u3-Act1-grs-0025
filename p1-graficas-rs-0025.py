import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Emily Barraza NC = 0025

#crearemos nuestra tabla y la guardaremos con pandas
# tenemos 5 listas de redes sociales con 4 elementos por lista
fb = ['Facebook', 8833, True, 2006]
twt = ['Twitter', 8575, False, 2008]
ig = ['Instagram', 7575, True, 2010]
wsp = ['Whatsapp', 8828, True, 2009]
tel = ['Telegram', 2992, False, 2010]
lkn = ['Linkdin', 7277, False, 2012]
# Creamos una lista de listas
lista_redes_sociales=[fb , twt, ig, wsp, tel, lkn]
print(lista_redes_sociales)
# Utilizar panda para utilizar la tabla (DataFrame o marco de datos)
# A cada columna le ponemos nombre
df_redes_sociales=pd.DataFrame(lista_redes_sociales,columns=["Nombre","Cantidad","Es_FB","Año"])
print(df_redes_sociales)
# creamos el archivo CSV y lo guardamos en CSV
df_redes_sociales.to_csv("redessociales.csv", index=False)
# crear grafica de lineas 
# donde x es Nombre es el eje horizontal
# donde y es cantidad es el eje vertical
plt.plot(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.title("Grafica redes sociales 0025")
plt.xlabel("Nombre de las redes")
plt.ylabel("cantidad de usuarios")
plt.show()

# creamos una grafica de puntos 
plt.scatter(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.title("Redes Sociales 0025")
plt.xlabel("Las redes")
plt.ylabel("Cantidad de usuario")
plt.show()
# Grafica de barras
plt.bar(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.title("Redes Sociales 0025")
plt.xlabel("Las redes")
plt.ylabel("Cantidad de usuario")
plt.show()
# Ordenar la grafica de manera descendente
# De la más grande a la más pequeña
df_rs_ordenar=df_redes_sociales.sort_values("Cantidad",ascending=False)
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"])
plt.show()
# coloreando grafica
df_rs_ordenar=df_redes_sociales.sort_values("Cantidad",ascending=False)
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"],
        color=["b","g","c","m","y","r"]
)
plt.show()
# Grafica de pastel 
#plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"])
plt.pie(df_redes_sociales["Cantidad"],labels=df_redes_sociales["Nombre"])
plt.show()