import requests
import json

# Lista donde se guardarán los resultados
resultados = []

print("Consulta información de una IP pública. Escribe 'exit' para salir.\n")

# Ciclo principal del programa
while True:
    ip = input("Escribe una IP pública: ")

    # Si el usuario escribe 'exit', salimos del programa
    if ip.lower() == "exit":
        break

    # Hacemos la solicitud a la API
    url = f"http://ip-api.com/json/{ip}"
    respuesta = requests.get(url)
    datos = respuesta.json()

    # Verificamos si la IP es válida
    if datos["status"] == "success":
        # Extraemos y mostramos la información
        pais = datos["country"]
        region = datos["regionName"]
        isp = datos["isp"]
        lat = datos["lat"]
        lon = datos["lon"]

        print(f"País: {pais}")
        print(f"Región: {region}")
        print(f"ISP: {isp}")
        print(f"Coordenadas: {lat}, {lon}\n")

        # Guardamos la información en una lista
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

# Guardamos todos los resultados en un archivo JSON
with open("resultados_ips.json", "w") as archivo:
    json.dump(resultados, archivo, indent=4)

print("\n¡Programa terminado! Los resultados se guardaron en 'resultados_ips.json'.")
