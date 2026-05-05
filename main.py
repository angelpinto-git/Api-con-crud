import requests

url = "https://jsonplaceholder.typicode.com/posts"

def safe_request(method, url, **kwargs):
    try:
        response = requests.request(method, url, timeout=5, **kwargs)
        
        # Lanza excepción si el status no es 2xx
        response.raise_for_status()
        
        # Intentar parsear JSON
        try:
            return response.json()
        except ValueError:
            print("Error: la respuesta no es JSON válido")
            return None

    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err} - Status code: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("Error de conexión")
    except requests.exceptions.Timeout:
        print("La petición tardó demasiado (timeout)")
    except requests.exceptions.RequestException as err:
        print(f"Error inesperado: {err}")
    
    return None


# GET obtener
def obtener_posts():
    data = safe_request("GET", url)
    if data:
        print(data[:2])

# POST
def crear_post():
    title = input("Título del post: ")
    body = input("Contenido del post: ")
    user_id = input("ID del usuario: ")

    # Validación básica opcional
    try:
        user_id = int(user_id)
    except ValueError:
        print("El userId debe ser un número")
        return

    new_post = {
        "title": title,
        "body": body,
        "userId": user_id
    }

    data = safe_request("POST", url, json=new_post)
    if data:
        print("Post creado:")
        print(data)

# PUT
def actualizar_post(id):
    title = input("Nuevo título del post: ")
    body = input("Nuevo contenido del post: ")
    user_id = input("Nuevo ID del usuario: ")

    # Validación básica
    try:
        user_id = int(user_id)
    except ValueError:
        print("El userId debe ser un número")
        return

    update_post = {
        "id": id,
        "title": title,
        "body": body,
        "userId": user_id
    }

    data = safe_request("PUT", f"{url}/{id}", json=update_post)
    if data:5

        print("Post actualizado:")
        print(data)

# DELETE
def eliminar_post(id):
    try:
        response = requests.delete(f"{url}/1", timeout=5)
        response.raise_for_status()
        print(f"DELETE exitoso. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
         print(f"Error en DELETE: {e}")


def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Ver posts")
        print("2. Crear post")
        print("3. Actualizar post")
        print("4. Eliminar post")
        print("5. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            obtener_posts()
        elif opcion == "2":
            crear_post()
        elif opcion == "3":
            post_id = int(input("ID del post: "))
            actualizar_post(post_id)
        elif opcion == "4":
            post_id = int(input("ID del post: "))
            eliminar_post(post_id)
        elif opcion == "5":
            break
        else:
            print("Opción inválida")

menu()
