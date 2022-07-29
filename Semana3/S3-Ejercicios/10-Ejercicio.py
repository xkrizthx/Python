def contar_palabras(nombre):
    cant_palabras=len(nombre.split())
    return cant_palabras


#Crear Listas vacias
lista_nombre=[]
lista_palabras=[]
#llenado de la lista
nombre=input('Nombre completo :')
while nombre!='FIN':
    lista_nombre.append(nombre)
    nombre=input('Nombre completo :')

#Procesar los datos de la lista
for x in lista_nombre:
    cant_palabras=contar_palabras(x)  #<--Funcion
    lista_palabras.append(cant_palabras)

#imprimir
print(lista_nombre)
print(lista_palabras)

for i in range(len(lista_palabras)):
    print(f'El Nombre[{i}]:',lista_nombre[i], 'tiene ',lista_palabras[i],' palabras')

    