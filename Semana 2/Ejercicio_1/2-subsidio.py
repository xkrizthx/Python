empleado = input('Ingrese el nombre del empleado: ')
salario = float(input('Ingrese el salario del empleado:'))
if (salario<=1000000):
        subsidios = 120000
else:
    subsidio=0 
print(' ****** Impresion de los Datos del Trabajador *****');
print('Nombre del Trabajador: ',empleado);
print('El salario del Trabajador: ','{:,.2f}'.format(salario));
print('El subsidio del trabajador: ','{:,.1f}'.format(subsidios));