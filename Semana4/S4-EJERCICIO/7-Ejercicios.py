'''
frase = "Cuando algo es lo suficientemente importante,
         lo haces incluso si las probabilidades de que salga bien no te acompañan"
'''
#palabra1 = "éxito"  #leer por pantalla
#palabra2 = "tecnología"

#Si alguna de las dos palabras se encuentra en el texto
'''
frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1=input('Ingrese palabra1 a buscar en el texto ')
palabra2=input('Ingrese palabra2 a buscar en el texto ')
estado= palabra1 not in frase or palabra2 not in frase 
print(estado)
'''



alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
'''
Saludar a cada persona de esta forma:
     Hola Maria
     Hola Jose
     Hola Carlos
   
for alumnos in range(len(alumnos_clase)):
    print(f'Hola {alumnos_clase[alumnos]}')

lista_numeros = [1,50,8,73,65,-8]
               # 0  1  2 3  4  5  6
mayor=max(lista_numeros)
menor=min(lista_numeros)
sumatoria=sum(lista_numeros)
print(mayor)
print(menor)
print(sumatoria)
''' 
lista_numeros = [1,50,8,73,65,-8]
mayor=0
menor=0
print(len(lista_numeros))
for numeros in range(0,len(lista_numeros)):
    print(numeros)
    if lista_numeros[numeros]>mayor:
        mayor=lista_numeros[numeros]
        posmay=numeros

print(f'Mayor {posmay}')    
    

