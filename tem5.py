ARCHIVO="contactos.txt"

#Ingresar datos por teclado.
def ingresar_contacto():
    id = input("Ingrese ID: ")
    nombre = int(input("Nombre: "))
    telefono = float(input("Teléfono: "))
    return id, nombre, telefono
    
# Añadir nuevos registros sin sobrescribir los anteriores
def guardar_contacto():
    id_contacto, nombre, telefono = ingresar_contacto()
    
    with open(ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(f"{id_contacto},{nombre},{telefono}\n")
    print("Contacto guardado correctamente.")
