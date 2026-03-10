# Entrada de datos 
n = int(input('Ingrese un número entero: '))

'''
if n % 2 == 0:
    print('Es par')
else:
    print('Es impar')
'''

if n > 0:
    print('Es Par positivo' if n % 2 == 0 else 'Es Impar Positivo')
elif n < 0:
    print('Es Par negativo' if n % 2 == 0 else 'Es Impar Negativo')
else:
    print('El número es cero')

#salida = 'Es par' if n % 2 == 0 else 'Es impar'