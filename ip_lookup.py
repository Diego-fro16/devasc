import requests
import json

def get_ip_info(ip):
    url = f'https://ipinfo.io/{ip}/json'
    try:
        response = requests.get(url)
        data = response.json()

     
        info = {
            "IP": ip,
            "Pais": data.get("country", "Desconocido"),
            "Region": data.get("region", "Desconocido"),
            "ISP": data.get("org", "Desconocido"),
            "Coordenadas": data.get("loc", "Desconocidas")
        }

        return info
    except Exception as e:
        print(f"Error al obtener la información de la IP: {e}")
        return None

def main():
    resultados = []
    
    while True:
        ip = input("Introduce la IP pública (o escribe 'exit' para salir): ")

        if ip.lower() == "exit":
            break

        info = get_ip_info(ip)

        if info:
            print(f"\nDatos de la IP {ip}:")
            print(f"Pais: {info['Pais']}")
            print(f"Region: {info['Region']}")
            print(f"ISP: {info['ISP']}")
            print(f"Coordenadas Geográficas: {info['Coordenadas']}")
            
            resultados.append(info)

   
    with open("ip_info.json", "w") as f:
        json.dump(resultados, f, indent=4)

    print("\nResultados guardados en 'ip_info.json'.")

if __name__ == "__main__":
    main()
