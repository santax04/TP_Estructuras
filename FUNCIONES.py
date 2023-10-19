def editar_archivo(nombre_archivo, nuevo_usuario , nueva_contraseña):
    try:
        with open(nombre_archivo, "a") as archivo:
            archivo.write(nuevo_usuario+ " " + nueva_contraseña + "\n" )
        print("Archivo editado con éxito.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al editar el archivo: {str(e)}")

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    return lineas

def crear_diccionario(nombre_archivo):
    diccionario = {}
    lineas = leer_archivo(nombre_archivo)
    for linea in lineas:
        usuario, contraseña = linea.strip().split()
        diccionario[usuario] = contraseña
    return diccionario