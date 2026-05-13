'''
Clasificador de números
Objetivo
Crear un programa que solicite un número entero y determine si es
- Positivo.
- Negativo.
- Cero.
- Par.
- Impar.
Requisitos

El programa debe:

1. Pedir un número entero.
2. Evaluar si el número es positivo, negativo o cero.
3. Evaluar si el número es par o impar.
4. Mostrar los resultados en pantalla.
'''
numero = 0
numero = int(input('Ingrese el numero a evaluar :'))
if (numero > 0):
    print(f'El numero {numero} es positivo')
elif (numero < 0):
    print(f'El numero {numero} es negativo')
else:
    print(f'El numero {numero} es Cero')

if(numero % 2 == 0):
    print(f'El numero {numero} es Par')
else:
    print(f'El numero {numero} es Impar')

