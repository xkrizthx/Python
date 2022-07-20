numero = int(input('Ingrese el numero para la tabla de multiplicar:'))
tope = int(input('Hasta que tope quiere calcular la tabla: '))
for i in range(1,tope):
    print(f'{i}*{numero}={i*numero}')
    
print('Finalizado')