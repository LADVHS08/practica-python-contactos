ARCHIVO="contactos.txt"

#Ingresar datos por teclado.
def ingresar_contacto():
    id_contacto = input("Ingrese ID: ")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    return id_contacto, nombre, telefono
    
# Añadir nuevos registros sin sobrescribir los anteriores
def guardar_contacto():
    id_contacto, nombre, telefono = ingresar_contacto()
    
    with open(ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write("\t".join([id_contacto, nombre, telefono]) + "\n")
    print("Contacto guardado correctamente.")
