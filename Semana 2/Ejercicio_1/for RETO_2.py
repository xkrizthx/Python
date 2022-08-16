N=int(input("Ingrese el número de productos a procesar: " ))

valor_total_compra=0
valor_total_IVA=0
for i in range (1,N+1):
    print(f"Datos producto: {i}")
    codigo=int(input ("Ingrese el código del producto: "))
    nombre=str(input ("Ingrese el nombre del producto: "))
    cantidad=int(input ("Ingrese la cantidad comprada: "))
    valor_unitario=float(input ("Ingrese el valor unitario: "))
    tipo_de_IVA=int(input("Ingrese el tipo de IVA [1-Excento de IVA, 2-Bienes, 3-General] "))
    valor_producto=cantidad*valor_unitario
    if tipo_de_IVA==1:
       valor_IVA=0
    elif tipo_de_IVA==2:        
       valor_IVA=valor_producto*0.05
    else:
       valor_IVA=valor_producto*0.19
    total_a_cobrar=valor_producto+valor_IVA
    print("----------------------------------------------------------------")
    print("El valor del producto es: \nCodigo: {} \nNombre: {} \nValor total sin IVA: {} \nvalor total: {}".format(codigo,nombre,total_a_cobrar,valor_IVA))
    print("----------------------------------------------------------------")
    valor_total_compra=valor_total_compra+total_a_cobrar
    valor_total_IVA=valor_total_IVA+valor_IVA


print("------------------------------------------")
print(f"El valor total de la compra es : {valor_total_compra}")
print(f"El valor total del IVA es : {valor_total_IVA}")