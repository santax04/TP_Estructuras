class Usuario:
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contrasenia = contraseña

    def crear_usuario(self):
        self.usuario = input("INGRESE USUARIO: ")
        self.contrasenia = input("INGRESE CONTRASEÑA: ")