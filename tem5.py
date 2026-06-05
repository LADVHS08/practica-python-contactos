ARCHIVO="contactos.txt"

# Escribir los datos en un archivo de texto
def escribir_contacto():
    id_contacto, nombre, telefono = ingresar_contacto()

    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        # Encabezado
        archivo.write("\t".join(["ID", "Nombre", "Telefono"]) + "\n")
        # Registro
        archivo.write("\t".join([id_contacto, nombre, telefono]) + "\n")
    print("Datos escritos correctamente.")
