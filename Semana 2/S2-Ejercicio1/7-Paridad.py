contP=0
contI=0
numero=int(input('Ingrese numero a calcular la paridad '))
while (numero!=-1):
    if numero%2==0:
        contP+=1
    else:
        contI+=1
    numero=int(input('Ingrese numero a calcular la paridad '))
print(f'Total Pares:{contP}')
print(f'Total Impares:{contI}')

