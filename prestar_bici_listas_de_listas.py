usuarios = [['ddd', 'dafault', 'default'], ['vvv', 'dafault', 'default']]
viajes = []

def mostrar_menu():
    # Menu principal
    print('''
    Bienvenido a PRESTA UNA BICI

    1. Registrar usuario
    2. Ingresar
    3. Salir
    ''')

    opcion = input('Elija una opción: ')

    if opcion == '1':
        registrar_usuario()
    elif opcion == '2':
        ingresar()
    elif opcion == '3':
        print('Saliendo...')
        exit()
    else:
        print('Opción inválida.')
        mostrar_menu()

def registrar_usuario():
    # Datos del usuario
    correo = input('Ingrese su correo electrónico: ')
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')

    # Verificar si ya existe
    for usuario in usuarios:
        if usuario[0] == correo:
            # El usuario existe
            print('El usuario ya existe.')
            mostrar_menu()
            return

    # Agregar a la lista
    usuarios.append([correo, nombre, apellido])

    print('Usuario registrado con éxito.')
    mostrar_menu()

def ingresar():
    correo = input('Ingrese su correo electrónico: ')

    # Ver si existe
    for usuario in usuarios:
        if usuario[0] == correo:
            break
    else:
        print('El usuario no existe.')
        mostrar_menu()
        return

    # Menu del usuario
    print('''
    Menú de usuario

    1. Hacer un viaje
    2. Ver mis viajes
    ''')

    opcion = input('Elija una opción: ')

    if opcion == '1':
        hacer_viaje(usuario)
    elif opcion == '2':
        ver_viajes(usuario)
    else:
        print('Opción inválida.')
        ingresar()

def hacer_viaje(usuario):
    # viaje
    lugar_salida = input('Ingrese el lugar de salida: ')
    lugar_llegada = input('Ingrese el lugar de llegada: ')
    fecha = input('Ingrese la fecha (YYYY-MM-DD): ')

    viajes.append([usuario[0], lugar_salida, lugar_llegada, fecha])

    print('Viaje registrado con éxito.')
    ingresar()

def ver_viajes(usuario):
    print('''
    Viajes del usuario:
    ''')
    for viaje in viajes:
        if viaje[0] == usuario[0]:
            print(f'    Lugar de salida: {viaje[1]}')
            print(f'    Lugar de llegada: {viaje[2]}')
            print(f'    Fecha: {viaje[3]}')
    print('''
    Fin de los viajes.
    ''')
    ingresar()

mostrar_menu()