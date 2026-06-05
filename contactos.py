def mostrar_contactos():
    try:
        with open(ARCHIVO, "r") as archivo:
            print("\n--- CONTACTOS REGISTRADOS ---")

            for linea in archivo:
                print(linea.strip())

    except FileNotFoundError:
        print("No existe el archivo.")