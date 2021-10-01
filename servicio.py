import requests
import os
import time

"""
os.system("cls")
while True:
    r = requests.get("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
    data = r.json()
    dolart = data[0]["casa"]["venta"]
    dolart = dolart.replace(",",".")
    dolar = float(dolart)
    print("Dolar oficial: ", dolar)
    print("Dolar oficial con impuestos: ", dolar*1.3*1.35)
    time.sleep(20)
    os.system("cls")
"""


#api.openweathermap.org/data/2.5/weather?id=Buenos%20Aires,AR&units=metric&appid=nfew8ry438ew83yr8q3yh83wy38y38

r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Buenos%20Aires,AR&units=metric&appid=")
data = r.json()

temperatura = data["main"]["temp"]
humedad = data["main"]["humidity"]
presion = data["main"]["pressure"]
visibilidad = data["visibility"]
nubes = data["clouds"]
ciudad = data["name"]


if humedad > 70 and presion < 1013 and visibilidad < 10000 and nubes > 0:
    print("En",ciudad,"la tempera actual es:",temperatura)
    print("Hay cierta posibilidad de lluvias")
else:
    print("En",ciudad,"la tempera actual es:",temperatura)
    print("No hay posibilidad de lluvias")