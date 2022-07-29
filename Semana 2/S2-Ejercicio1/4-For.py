numero=int(input('Ingrese el numero para el cual quiere calcular la tabla de multiplicar '))
tope=int(input('hasta que tope quiere calcular la tabla '))
for i in range(1,tope,1):
    print(f'{i}*{numero}={i*numero}')
    
print('Finalizado')