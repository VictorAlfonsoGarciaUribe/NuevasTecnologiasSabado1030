#Tenemos ingresos y egresos en listas separadas 
# Que a medida que vamos ingresando o retirando el nos da sado 
# saldo no puede ser negativo
# No puede retirar mas de lo que tiene en saldo o cuando el saldo es cero


# Inicialización de listas de ingresos y egresos
ingresos = []
egresos = []

# Función para imprimir recibo
def imprimir_recibo(tipo, monto):
    print("")
    print("")
    print("")
    print("***** Recibo *****")
    print(f"Tipo de movimiento: {tipo}")
    print(f"Monto: {monto}")
    print("********************")

# Función para mostrar hoja ordenada de movimientos
def mostrar_movimientos():
    print("")
    print("")
    print("")
    print("***** Hoja de Movimientos *****")
    print("Ingresos:")
    for ingreso in ingresos:
        print(f"Ingreso: {ingreso}")
        
    print("------------------------")
    print("Egresos:")
    for egreso in egresos:
        print(f"Egreso: {egreso}")
    print("*******************************")

# Inicia saldo
saldo = 0

# Menú principal
while True:
    print("")
    print("")
    print("")
    print("----- Menú -----")
    print("1. Consignación")
    print("2. Retiro")
    print("3. Mostrar Movimientos")
    print("4. Salir")
    print("")
    print(f"Saldo actual: {saldo}")
    print("")
    print("")
    print("")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        monto = float(input("Ingrese el monto de la consignación: "))
        ingresos.append(monto)
        saldo += monto
        imprimir_recibo("Consignación", monto)

    elif opcion == 2:
        monto = float(input("Ingrese el monto del retiro: "))
        if monto <= saldo:
            egresos.append(monto)
            saldo -= monto
            imprimir_recibo("Retiro", monto)
        else:
            print("Saldo insuficiente para el retiro.")

    elif opcion == 3:
        mostrar_movimientos()

    elif opcion == 4:
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")