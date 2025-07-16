import requests
import json

resultados = []

print("Consulta información de una IP pública. Escribe 'exit' para salir.\n")

while True:
    ip = input("Escribe una IP pública: ")

    if ip.lower() == "exit":
        break

    url = f"http://ip-api.com/json/{ip}"
    respuesta = requests.get(url)
    datos = respuesta.json()

    if datos["status"] == "success":
        pais = datos["country"]
        region = datos["regionName"]
        isp = datos["isp"]
        lat = datos["lat"]
        lon = datos["lon"]

        print(f"País: {pais}")
        print(f"Región: {region}")
        print(f"ISP: {isp}")
        print(f"Coordenadas: {lat}, {lon}\n")

        resultado = {
            "ip": ip,
            "pais": pais,
            "region": region,
            "isp": isp,
            "coordenadas": {
                "latitud": lat,
                "longitud": lon
            }
        }
        resultados.append(resultado)
    else:
        print("IP no válida o no se pudo obtener información.\n")

with open("resultados_ips.json", "w") as archivo:
    json.dump(resultados, archivo, indent=4)

print("\n¡Programa terminado! Los resultados se guardaron en 'resultados_ips.json'.")
