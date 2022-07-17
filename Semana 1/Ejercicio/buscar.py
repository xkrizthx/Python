print('* Bienvenido al sistema de notas *')
nombre=str(input('Ingrese su Nombre: '))
apellido=str(input('Ingrese su Apellido: '))
edad=str(input('Ingrese su Edad: '))
data=nombre +' '+ apellido +' '+  edad
print(data)
valida=data.index(input('Ingrese el Apellido a buscar: '))
print(valida)
extrae=data[valida:]
print (extrae)

