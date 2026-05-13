# Contador de 1 a 20
def contarNros(inicio):
    print(inicio, end = ' ')
    if(inicio < 20):
        contarNros(inicio+1)

contador = 1
contarNros(contador)
# while(contador <= 20):
#     print(contador,end=' ')
#     contador +=1