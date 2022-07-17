codigo = int(input ( 'Ingrese el codigo del estudiante: '))
nombre = str(input ( 'Ingrese el nombre del estudiante: '))
nota1 = float(input( 'Ingrese la nota 1: '))
nota2 = float(input( 'Ingrese la nota 2: '))
definitiva =(nota1+nota2)/2
print('El codigo del estudiante es  {} \n con nombre {} \n y su definitiva es {}'.format(codigo,nombre,round(definitiva,1)))
