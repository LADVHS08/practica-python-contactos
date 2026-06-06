# Función para leer y procesar datos
def procesar_datos():
    try:
        contactos = []
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            next(archivo)
            for linea in archivo:
                contactos.append(linea.strip().split("\t"))

        # Búsqueda
        buscar = input("Ingrese el nombre que desea buscar: ")
        encontrado = False
        for contacto in contactos:
            if contacto[1].lower() == buscar.lower():
                print("\nContacto encontrado:")
                print(f"ID: {contacto[0]}")
                print(f"Nombre: {contacto[1]}")
                print(f"Teléfono: {contacto[2]}")

                encontrado = True
                break

        if not encontrado:
            print("Contacto no encontrado.")

        # Conteo
        print(f"\nCantidad total de contactos: {len(contactos)}")

    except FileNotFoundError:
        print("No existe el archivo.")
