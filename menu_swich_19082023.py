#variable opcion 
#if opcion = 1 instrucción 
#elif opcion = 2
#elif opcion 3 = Salir
#else "Seleccione una opcion valida"

while True:
    print("Menú:")
    print("1. Tarjetas de crédito")
    print("2. Más")
    print("3. Volver")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("Has seleccionado 'Tarjetas de crédito'")
        # importamos el archivo ejercicio_tarjeta_de_c_19082023.py
        from ejercicio_tarjeta_de_c_19082023 import procesar_compra

        # Solicitar los valores de compra y cuotas al usuario
        compra = float(input("Valor de compra: $"))
        cuotas = int(input("Número de cuotas: "))

        # Llamar a la función 
        procesar_compra(compra, cuotas)
        continue
        
    elif opcion == "2":
        print("Has seleccionado 'Más'")
        # Aquí podrías poner el código relacionado con la opción 2
    elif opcion == "3":
        print("Volviendo al menú principal...")
        # Aquí podrías poner el código relacionado con la opción 3
    else:
        print("Opción incorrecta. Por favor, selecciona una opción válida.")
        continuar = input("¿Quieres salir del programa? (si/no): ")
    if continuar.lower() == "si":
        print("Saliendo del programa.")
        break