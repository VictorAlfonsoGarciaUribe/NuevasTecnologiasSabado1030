#simular una tarjeta de credito que pide valor y cuotas 
#usar el ciclo while disminuye el valor adeudado cada que paga 1 cuota
#el ciclo termina cuando las cuotas llegan a 0 o cuando deuda = 0 imprime tarjeta pagada 
#preguntar al  

##En el codigo sin funcion los siguientes eran los imput, ahora estos pasan a ser llamados desde el menu 
#compra = float(input("Valor de compra: $"))
#cuotas = int(input("Número de cuotas: "))

def procesar_compra(compra, cuotas):
    estado = True
    deuda = compra
    saldo = 0
    pago = 0
    valor_cuota = compra / cuotas
    print(f"El valor de cuota mínimo es {valor_cuota:.2f}")

    if valor_cuota > deuda:
        valor_cuota = deuda
    else:
        valor_cuota = valor_cuota

    while estado:
        if deuda > 0:
            if cuotas > 0:
                pagar_minimo = input("¿Deseas pagar el mínimo? (si / otro): ")

                if pagar_minimo.lower() == "si":
                    deuda -= valor_cuota
                    print(f"Valor pagado {valor_cuota:.2f} valor deuda {deuda:.2f}")
                else:
                    pago = float(input("Ingrese el monto a pagar: $"))

                if pago > deuda:
                    print("El monto ingresado es mayor que la deuda restante.")
                    continue

                deuda -= pago
                cuotas -= 1
                saldo += pago

                print(f"Deuda restante: ${deuda:.2f}")
                print(f"Cuotas restantes: {cuotas}")
            else:
                print("Tarjeta pagada.")
                cuotas = 0
                deuda = 0
                estado = False
        else:
            print("Tarjeta pagada.")
            cuotas = 0
            deuda = 0
            estado = False
