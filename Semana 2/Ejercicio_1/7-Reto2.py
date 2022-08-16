prod = int(input('Ingrese la cantdad de productos:'))
i = 0
sub = 0
while i < prod:
    codigo =int(input(f'Ingrese el codigo del producto {i+1}: '))
    nombre =str(input(f'Ingrese el nombre del producto {i+1}: '))
    cant = int(input(f'Ingrese la cantidad de producto {i+1}: '))
    valorU = float(input(f'Ingrese el Valor Unitario {i+1}: '))
    iva=input(f'Digite el Tipo de iva [E=Exento, B=Bienes, G=General]: ')
    valorsiniva = float(valorU * cant)
    sub = sub + valorsiniva
    i += 1
    
    if iva == 'B':
        iva_prod = valorsiniva * 0.05
        
    elif iva == 'G':
        iva_prod = valorsiniva * 0.19
    else:
        iva_prod = valorsiniva
    print ('El codigo del Producto es:',codigo)
    print ('El nombre del Producto es:',nombre)
    print ('El valor sin iva del Producto es:',valorsiniva)
    print ('El iva del producto del Producto es:',iva_prod)   
total = sub + iva_prod
print("Se vendieron: " ,prod, "Productos")
print ("Subtotal es: ", sub)
print ("Total: ", total)
print ("El Iva total es: ",iva_prod)
