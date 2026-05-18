from colorama import Fore, Style, init

from services.posts import (
    obtener_posts,
    crear_post,
    actualizar_post,
    eliminar_post
)

init(autoreset=True)


def menu():
    while True:
        print(f"\n{Fore.BLUE}=== MENÚ ===")
        print(f"{Fore.GREEN}1. Ver posts")
        print(f"{Fore.GREEN}2. Crear post")
        print(f"{Fore.GREEN}3. Actualizar post")
        print(f"{Fore.GREEN}4. Eliminar post")
        print(f"{Fore.RED}5. Salir")

        opcion = input(
            f"{Fore.BLUE}Seleccione una opción: {Style.RESET_ALL}"
        )

        match opcion:

            case "1":
                obtener_posts()

            case "2":
                crear_post()

            case "3":
                try:
                    post_id = int(input("ID del post: "))
                    actualizar_post(post_id)
                except ValueError:
                    print("ID inválido")

            case "4":
                try:
                    post_id = int(input("ID del post: "))
                    eliminar_post(post_id)
                except ValueError:
                    print("ID inválido")

            case "5":
                print("Saliendo...")
                break

            case _:
                print("Opción inválida")