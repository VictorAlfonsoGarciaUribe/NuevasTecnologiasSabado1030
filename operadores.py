#1. Validar que una compra se va a pagar por un valor x y si incluye o no propina 

valor = input ("Valor a pagar: $_")
pago = input("Va a pagar (si/no) :")
propina = input("incluir propina (si/no) :")

if (pago.lower() == 'si' and propina.lower() == 'si'):
    print(f"el pago es de $ {float(valor) * 1.10}")
elif (pago.lower() == 'si' and propina.lower() == 'no'):
    print(f"el pago es de $ {valor}")
else: 
    print("suerte")
    

#2. Simular un login que capture los datos y despues se registre 

print ('******* Registro de nuevo cliente ******* ')
cliente = {}
cliente ['nombre'] = input("Registre nombre: ")
cliente ['email']= input("Coreeo electronico: ")
cliente ['telefono']= input("Telefono")
cliente ['contraseña'] = input("contraseña")

captcha = 6

print ('******* Login ******* ')
val_inicio = input("Email o Telefono: ")
val_contraseña = input("Contraseña: ")
val_captcha = input("Digito infernal: ")

print (cliente)

if (cliente.email == val_inicio or cliente.telefono == val_inicio  ):
    if (cliente.contraseña == val_contraseña and captcha == val_captcha):
        print (f"bienvenido {cliente.nombre}")
    else:
        print("Informacion incorrecta")
else:
        print("Cliente no existe")
        