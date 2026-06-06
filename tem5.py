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
