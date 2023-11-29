import json
import requests

def obtener_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    print(url)
    respuesta = requests.get(url, params={'results': 1})
    print(respuesta.status_code)

    return json.loads(respuesta.content)

def obtener_nacionalidad(nombre):
    url = "https://api.nationalize.io"
    print(url)
    respuesta = requests.get(url, params={'name': nombre})
    print(respuesta.status_code)

    return json.loads(respuesta.content)

def obtener_prediccion_edad(nombre):
    url = "https://api.agify.io"
    print(url)
    respuesta = requests.get(url, params={'name': nombre})
    print(respuesta.status_code)

    return json.loads(respuesta.content)
  
if __name__ == "__main__":
    nombre = input("Ingrese un nombre por favor: ")
    dua = obtener_usuario_aleatorio()
    print("Datos de Usuario Aleatorio:")
    print(json.dumps(dua, indent=2))
          
    dn = obtener_nacionalidad(nombre)
    print("\nPredicción de Nacionalidad:")
    print(json.dumps(dn, indent=2))
    
    dpe = obtener_prediccion_edad(nombre)
    print("\nPredicción de Edad:")
    print(json.dumps(dpe, indent=2))
    