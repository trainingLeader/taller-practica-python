import os
def saludar(nombre):
    print(f'Hola {nombre} estas en la clase mas relajante del mundo')
    os.system('pause')
def msgMotiva(nombre):
    print(f'{nombre} Animo...No te preocupes si no sabes \nprogramar...Aqui te enseñamos con I(Insomnio) y A(Angustia)')
    os.system('pause')
menu = '''
1. Saludar
2. Mostrar mensaje motivacional
3. Mostrar autor del programa
4. Salir
'''
opcion =0
while (True):
    os.system('cls') #clear
    print(menu)
    opcion=int(input(':() '))
    match(opcion):
        case 1:
            nombre = input('Ingrese su nombre :')
            saludar(nombre)
        case 2:
            nombre = input('Ingrese su nombre :')
            msgMotiva(nombre)
        case 3:
            print('Autorrrr')
            os.system('pause')
        case 4:
            break
        case _:
            print('Opcion no valida')
            os.system('pause') # x=input('....')