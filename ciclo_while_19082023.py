#inicio
#dato
#condicion
#instrucción
#si se cumple la condición vuelve a la instrucción
#si se deja de cumplir la condicion sale 
#fin

import random

vida = 5

puntos = 0

while (vida != 0):
    
    num= random.randint(0,9)
    
    if num==0:
        vida-=1
        print (f"Vidas: {vida}")
    else:
        puntos +=1
        print (f"Puntos: {puntos}")