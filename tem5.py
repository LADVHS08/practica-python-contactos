ARCHIVO="contactos.txt"

#Ingresar datos por teclado.
def ingresar_contacto():
    id_contacto = input("Ingrese ID: ")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    return id_contacto, nombre, telefono
  
# Escribir los datos en un archivo de texto
def escribir_contacto():
    id_contacto, nombre, telefono = ingresar_contacto()

    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        archivo.write("\t".join(["ID", "Nombre", "Telefono"]) + "\n")
        archivo.write("\t".join([id_contacto, nombre, telefono]) + "\n")
    print("Datos escritos correctamente.")

# Leer y mostrar el contenido del archivo línea por línea
def mostrar_contactos():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            print("\n--- CONTACTOS REGISTRADOS ---")

            for linea in archivo:
                print(linea.strip())

    except FileNotFoundError:
        print("No existe el archivo.")
        
# Añadir nuevos registros sin sobrescribir los anteriores
def guardar_contacto():
    id_contacto, nombre, telefono = ingresar_contacto()
    
    with open(ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write("\t".join([id_contacto, nombre, telefono]) + "\n")
    print("Contacto guardado correctamente.")

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

# Guardar contactos en archivo binario
def guardar_binario():
    contactos = []
    try:

        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            next(archivo)

            for linea in archivo:
                datos = linea.strip().split("\t")
                contacto = {
                    "id": datos[0],
                    "nombre": datos[1],
                    "telefono": datos[2]
                }
                contactos.append(contacto)

        with open(ARCHIVO_BINARIO, "wb") as archivo_binario:
            pickle.dump(contactos, archivo_binario)
        print("\nDatos guardados en archivo binario.")

    except FileNotFoundError:
        print("\nNo existe el archivo de texto.")

# Recuperar datos desde archivo binario
def leer_binario():
    try:
        with open(ARCHIVO_BINARIO, "rb") as archivo_binario:
            contactos = pickle.load(archivo_binario)
            print("\n=== CONTACTOS DESDE ARCHIVO BINARIO ===\n")

            for contacto in contactos:
                print("ID:", contacto["id"])
                print("Nombre:", contacto["nombre"])
                print("Teléfono:", contacto["telefono"])
                print("-" * 30)

    except FileNotFoundError:
        print("\nNo existe el archivo binario.")


# MENÚ PRINCIPAL
def menu():

    while True:

        print("\n=== SISTEMA DE GESTIÓN DE CONTACTOS ===")
        print("1. Registrar y escribir contacto")
        print("2. Mostrar contactos")
        print("3. Agregar contacto sin sobreescribir")
        print("4. Procesar datos")
        print("5. Guardar archivo binario")
        print("6. Leer archivo binario")
        print("7. Salir")

        opcion = input("Seleccione una opción:")

        if opcion == "1":
            escribir_contacto()
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "3":
            guardar_contacto()
        elif opcion == "4":
            procesar_datos()
        elif opcion == "5":
            guardar_binario()
        elif opcion == "6":
            leer_binario()
        elif opcion == "7":
            print("\nPrograma finalizado.")
            break
        else:
            print("\nOpción no válida.")

menu()
