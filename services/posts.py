from services.api import safe_request


def obtener_posts():
    data = safe_request("GET")

    if data:
        print("\nPrimeros posts:\n")

        for post in data[:2]:
            print(post)


def crear_post():
    title = input("Título: ")
    body = input("Contenido: ")

    try:
        user_id = int(input("User ID: "))
    except ValueError:
        print("User ID inválido")
        return

    payload = {
        "title": title,
        "body": body,
        "userId": user_id
    }

    data = safe_request("POST", json=payload)

    if data:
        print("\nPost creado:")
        print(data)


def actualizar_post(post_id):
    title = input("Nuevo título: ")
    body = input("Nuevo contenido: ")

    try:
        user_id = int(input("Nuevo User ID: "))
    except ValueError:
        print("User ID inválido")
        return

    payload = {
        "id": post_id,
        "title": title,
        "body": body,
        "userId": user_id
    }

    data = safe_request(
        "PUT",
        f"/{post_id}",
        json=payload
    )

    if data:
        print("\nPost actualizado:")
        print(data)


def eliminar_post(post_id):
    data = safe_request("DELETE", f"/{post_id}")

    if data == {}:
        print("Post eliminado correctamente")