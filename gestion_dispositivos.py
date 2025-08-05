import requests

API_URL = "https://reqres.in/api/users"

def agregar_dis(data):
    response = requests.post(API_URL, json=data)
    print("POST:", response.status_code, response.json())
    return response

def listar_dis():
    response = requests.get(API_URL)
    print("GET:", response.status_code, response.json())
    return response

def actualizar_dis(id, data):
    response = requests.put(f"{API_URL}/{id}", json=data)
    print("PUT:", response.status_code, response.json())
    return response

def eliminar_dis(id):
    response = requests.delete(f"{API_URL}/{id}")
    print("DELETE:", response.status_code)
    return response

# Ejemplos
if __name__ == "__main__":
    nuevo = {"name": "Router Cisco", "job": "Gateway"}
    agregar_dis(nuevo)
    listar_dis()
    actualizar_dis(2, {"name": "Router Actualizado", "job": "Firewall"})
    eliminar_dis(2)
