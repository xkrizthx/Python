articulos={1:"Lapiz",2:"Cuadernos",3:"Borrador",4:"Calculadora",5:"Escudadora"}
valores={1:2500,2:3800,3:1200,4:3500,5:3700}
N=int(input("Cuantos articulos deseas comprar :"))
total_compra=0;
for i in range(N):
    codigo=int(input("Codigo articulo :"))
    cantidad=int(input("Cantidad de articulos :"))
    valor_articulo=cantidad*valores.get(codigo)
    total_compra+=valor_articulo
    print('-----------------------------------')
    print('---- Salida de Datos ----')
    print('Nombre del articulo: ', articulos.get(codigo))
    print('Cantidad :',cantidad)
    print("Valor Unitario :","{:,.2f}".format(valores.get(codigo)))
    print("Valor de la Compra :","{:,.2f}".format(valor_articulo))
    print('-----------------------------------')

print("Valor Total Compra :","{:,.2f}".format(total_compra))
