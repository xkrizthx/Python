'''lista=list(range(5,25,2))
print(lista)

opcion='True'

while opcion:
    edad=int(input('Ingrese edad '))
    if edad>=18:
        print('Usted es mayor de edad ')
        break
    else:
        opcion=False
        continue
else:
    print('Usted es menor de edad ')
    
texto=input('Ingrese texto :') 
texto2=texto.split()
print(texto2)
lista=list(enumerate(texto,5))
#print(lista)

for indice,valor in enumerate(texto2):
    print(indice, valor)
    
letras=['a','b','c','d','e','f','g','h']
numeros=[1,2,3,4,5,6,7,8,9,10,11]
for letras, numeros in zip(letras, numeros):
    print(f'Letras {letras} con numeros {numeros}')
    
'''
diccionario={'Colombia':530,'EEUU':500,'Ecuador':3800}
lista=[4,25*2,6*(-1),0]
max1=max(diccionario.keys())
min2=min(diccionario.keys())
print(max1,' y ',min2)
max3=max(diccionario.values())
min4=min(diccionario.values())
print(max3, min4)
print(min(lista))
print(max(lista))