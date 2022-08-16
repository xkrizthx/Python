#Hacer un programa en Python que lea un rango de numeros
# y que calcule el cuadrado de cada uno.
#1,2,3,4,5,6,7,8,9,10,11
#1,4,9,16,25

mi_lista=list(range(1,10,1))
print(mi_lista)
for i in range(1,10):
    cuadrado=i**2
    print(cuadrado)

#Enumerate
#                0
lista_nombre=['Marlon','Pedro,','Maria','Luisa','jessica','Patricia','Mauricio','Salon']
            #  012345     0        0  
for indice, nombre in enumerate(lista_nombre):
    print(f'{nombre} se encuentra en el indice {indice}')

#Imprimir los nombres que solamente empiecen por M.
print("\n \n ")
print("Nombres que empiezan por M")

for indice, nombre in enumerate(lista_nombre):
    if nombre[0]=="M":
        print(f'{nombre} se encuentra en el indice {indice}')


#Imprimir los nombres que solamente empiecen por M.
print("\n \n")
print("Nombres que contienen una letra ")

for indice, nombre in enumerate(lista_nombre):
    if "o" in nombre:
        print(f'{nombre} se encuentra en el indice {indice}')


print("\n \n")
print(" Instruccion ZIP ")
#ZIP
marcas=["Nike","Lenovo","Nissan"]
productos=["Zapatilla","Portatil","Automoviles"]
precios=[250000,19800000,80000000]
mi_zip=zip(marcas,productos)
print(mi_zip)
for marca,producto,precio in zip(marcas,productos,precios):
    print(f'{marca} es una marc de {producto}, con un precio {precio}')

#Max y Min
print("\n \n")
print(" Instruccion Max y Min ")

lista=[25, 80, -25,78]
mayor=max(lista)
print(mayor)

lista2="Carl4os"
mayor2=max(lista2.lower())
print(mayor2)

diccionario={'c2':'Python', 'a2':'Java', 'b3':'C++'}
print(min(diccionario.values()))

diccionario2={'Carlos':25, 'Maria':18,'Pedro':43,'Luisa':17}

#edad_minima
print(min(diccionario2.values()))
print(max(diccionario2.keys()))
#Nombre mas alto de la lista del Alfabeto

