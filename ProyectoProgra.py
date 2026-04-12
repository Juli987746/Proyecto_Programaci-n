"""

Proyecto final para nuestro curso de progra

"""

# Acceso al sistema

usuarios_validos = ["Profesor1", "Profesor2", "Profesor3"]
password_correcta = "123"

def iniciosesion():
    intentos = 3

    while intentos > 0:
        print("Bienvenido, por favor ingresa tus credenciales")
        user = input("User: ")
        password = input("Password: ")

        if user in usuarios_validos:
        if password == password_correcta:
            print("Acceso concedido")
            acceso = "si"
        else:
            print("Contraseña incorrecta")
    else:
        print("Usuario incorrecto")
      
    if acceso == "no":
        intentos = intentos - 1
        print("Intentos restantes:", intentos)
    else:
        break

if acceso == "no":
  print("Acceso denegado")

