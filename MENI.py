from FUNCIONES import *
ejec = True
tipo = int(input("INGRESE TIPO DE USUARIO: 1.administrador, 2.cliente, 3.personal: "))
tipos = [1 , 2 , 3]
while tipo not in tipos:
    tipo = int(input("INGRESE TIPO NUEVAMENTE: (1.administrativo, 2.cliente, 3.personal)"))
existe = input("SI YA TIENIEN UN USUARIO INGESE 1, DE LO CONTRARIO OTRA TECLA")
if existe != "1":
    if tipo == 1:
        usuario = input("INGRESE USUARIO: ")
        contraseña = input("INGRESE CONTRASEÑA: ")
        editar_archivo("administrativos.txt", usuario , contraseña)
    if tipo == 2:
        usuario = input("INGRESE USUARIO: ")
        contraseña = input("INGRESE CONTRASEÑA: ")
        editar_archivo("cliente.txt", usuario , contraseña)
    if tipo == 3:
        usuario = input("INGRESE USUARIO: ")
        contraseña = input("INGRESE CONTRASEÑA: ")
        editar_archivo("personal.txt", usuario , contraseña)
else:
    if tipo == 1:
        diccionario = crear_diccionario("administrativos.txt")
        usuario = input("INGRESE USUARIO: ")
        while usuario not in diccionario.keys():
            usuario = input("USUARIO INCORRECTO, INGRESE NUEVAMENTE: ")
        contraseña = input("INGRESE CONTRASEÑA: ")
        while contraseña != diccionario[usuario]:
            contraseña = input("CLAVE INCORRECTA INGRESE NUEVAMENTE: ")
        
    if tipo == 2:
        diccionario = crear_diccionario("cliente.txt")
        usuario = input("INGRESE USUARIO: ")
        while usuario not in diccionario.keys():
            usuario = input("USUARIO INCORRECTO, INGRESE NUEVAMENTE: ")
        contraseña = input("INGRESE CONTRASEÑA: ")
        while contraseña != diccionario[usuario]:
            contraseña = input("CLAVE INCORRECTA INGRESE NUEVAMENTE: ")
    if tipo == 3:
        diccionario = crear_diccionario("personal.txt")
        usuario = input("INGRESE USUARIO: ")
        while usuario not in diccionario.keys():
            usuario = input("USUARIO INCORRECTO, INGRESE NUEVAMENTE: ")
        contraseña = input("INGRESE CONTRASEÑA: ")
        while contraseña != diccionario[usuario]:
            contraseña = input("CLAVE INCORRECTA INGRESE NUEVAMENTE: ")