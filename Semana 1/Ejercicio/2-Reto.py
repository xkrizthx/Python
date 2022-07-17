codigo = int(input('Ingrese su codigo: '))
nombre = str(input('Ingrese el nombre del producto: '))
cantidad = int(input('Ingrese la Cantidad: '))
valorU = int(input('Ingrese el Valor Unitario: '))

valorsiniva = float(valorU * cantidad)

total = valorsiniva * 1.19

print (codigo)
print (nombre)
print (valorsiniva)
print (total)
