nombre=input('Ingrese el nombre del trabajador :')
salario=float(input('Salario del trabajador :'))
if (salario<=1000000):
    subsidio=120000
else:
    subsidio=0
print(' ***** Impresion datos del Trabajador  ******')
print(f'Nombre del trabajador : {nombre}')
print("Salario del trabajador :",'{:,.1f}'.format(salario))
print("Subsidio del trabajador :",'{:,.1f}'.format(subsidio))                            