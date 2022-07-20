nombre= input('Ingrese su nombre: ')
estrato=int(input('Ingrese su estrato: '))
if estrato ==1:
    tarifa_bas='10000'
elif estrato == 2:
    tarifa_bas='15000'
elif estrato ==3:
    tarifa_bas='30000'
elif estrato ==4:
    tarifa_bas='50000'
else:
    tarifa_bas='65000'

print('Nombre ',nombre)
print('Su Estrato es: ',estrato)
print('Su tarifa basica es: ',tarifa_bas)