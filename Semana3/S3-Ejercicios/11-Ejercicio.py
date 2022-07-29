'''
matriz=[[1,2,3,4,5],[6,7,8,9,10]]        
print(matriz[1])
print(matriz[1][1:4])
'''
numeros=[]
cpares=0;
cimpares=0;
filas=int(input('Ingrese numero de filas :'))
columnas=int(input('Ingrese numero de Columnas :'))
for i in range(filas):
    numeros.append([])
    for j in range(columnas):
        numeros[i].append(int(input(f'Ingrese numero pos [{i}][{j}] :')))

print(numeros) 

#Contar los numeros pares e impares
print('***** Identificacion de Pares *****')
for i in range(filas):  #0
    for j in range(columnas): #0
        if numeros[i][j]%2==0:
            print(f'Numero par :{numeros[i][j]}')
            cpares+=1
        else:
            print(f'Numero Impar :{numeros[i][j]}')
            cimpares+=1
            
#Impresion:
print('***** Impresion de toda la lista *****')
for i in range(filas):  #0
    for j in range(columnas): #0 -1
        print(f'Dato[{i}][{j}]:',numeros[i][j])


print('***** Impresion de la estadistica *****')
print(f'Total pares :{cpares}')
print(f'Total Impares :{cimpares}')

