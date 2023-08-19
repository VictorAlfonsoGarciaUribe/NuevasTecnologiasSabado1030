#2. Simular un login que capture los datos y despues se registre 

print('******* Registro de nuevo cliente ******* ')
cliente = {}
cliente['nombre'] = input("Registre nombre: ")
cliente['email'] = input("Correo electrónico: ")
cliente['telefono'] = input("Teléfono: ")
cliente['contraseña'] = input("Contraseña: ")

captcha = 6

print('******* Login ******* ')
val_inicio = input("Email o Teléfono: ")
val_contraseña = input("Contraseña: ")
val_captcha = input("Código captcha: ")

if val_inicio == cliente['email'] or val_inicio == cliente['telefono']:
    if val_contraseña == cliente['contraseña']:
        if int(val_captcha) == captcha:
            print("Inicio de sesión exitoso.")
            print(cliente)
        else:
            print("Código captcha incorrecto. Inicio de sesión fallido.")
    else:
        print("Contraseña incorrecta. Inicio de sesión fallido.")
else:
    print("Email o Teléfono no encontrados. Inicio de sesión fallido.")