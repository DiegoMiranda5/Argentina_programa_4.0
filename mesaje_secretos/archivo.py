import csv

def abrir_archivo_escritura():
    """
        Abre el archivo para poder escribir al final del archivo
    """
    global archivo
    archivo = open("mensajes-cifrados.csv", "a", newline='') 

def abrir_archivo_lectura():
    global archivo
    archivo = open("mensajes-cifrados.csv", "r")

def cerrar_archivo():
    if archivo is None:
        print("Archivo cerrado")
    else:
        archivo.close()

def escribrir_en_archivo(registro):
    """
        Escribe un nuevo en el archivo en la ultima posicion de este
    """
    try:
        abrir_archivo_escritura()
        csvWriter = csv.writer(archivo, delimiter=',')
        csvWriter.writerows(registro)
        cerrar_archivo()
        print("Mensaje enviado")
    except Exception:
        print(f"Error al grabar")

def leer_en_archivo():
    """
        devuelve los registros existente en el archivo
    """
    try:
        abrir_archivo_lectura()
        csvRead = csv.reader(archivo)
        return csvRead
    except Exception:
        print("Error al leer el archivo")

archivo = None
