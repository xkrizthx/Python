from random import *
lista_nombres=['Juan','Pedro','Maria','Luisa','Fernanda','Oscar']
sorteo=choice(lista_nombres)
print(f'El ganador del sorteo es {sorteo}')

print(lista_nombres)
numeros=list(range(1,50,5))
print(numeros)
shuffle(lista_nombres)
shuffle(numeros)
print(numeros)
print(lista_nombres)