# Función para leer y procesar datos
def procesar_datos():
    # Leer datos
    nombres = []

    cantidad = int(input("¿Cuántos nombres desea ingresar?: "))

    for i in range(cantidad):
        nombre = input(f"Ingrese el nombre {i+1}: ")
        nombres.append(nombre)

    # Mostrar lista completa
    print("\nLista de nombres:")
    for nombre in nombres:
        print(nombre)

    # Búsqueda
    buscar = input("\nIngrese el nombre que desea buscar: ")

    if buscar in nombres:
        print(f"El nombre '{buscar}' sí se encuentra en la lista.")
    else:
        print(f"El nombre '{buscar}' no se encuentra en la lista.")

    # Conteo
    print(f"\nCantidad total de nombres ingresados: {len(nombres)}")


# Llamar a la función
procesar_datos()