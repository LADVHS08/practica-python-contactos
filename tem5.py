ARCHIVO="contactos.txt"

#Ingresar datos por teclado.
def ingresar_producto():
    nombre = input("Nombre del producto: ")
    stock = int(input("Stock: "))
    precio = float(input("Precio: "))
    return nombre, stock, precio

#Añadir nuevos registros sin sobrescribir los anteriores.
def guardar_producto():
    nombre, stock, precio = ingresar_producto()

    with open("inventario.txt", "a") as archivo:
        archivo.write(f"{nombre},{stock},{precio}\n")