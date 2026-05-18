import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


def safe_request(method, endpoint="", **kwargs):
    try:
        response = requests.request(
            method,
            f"{BASE_URL}{endpoint}",
            timeout=5,
            **kwargs
        )

        response.raise_for_status()

        try:
            return response.json()
        except ValueError:
            print("Error: respuesta JSON inválida")
            return None

    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")

    except requests.exceptions.ConnectionError:
        print("Error de conexión")

    except requests.exceptions.Timeout:
        print("Timeout excedido")

    except requests.exceptions.RequestException as err:
        print(f"Error inesperado: {err}")

    return None