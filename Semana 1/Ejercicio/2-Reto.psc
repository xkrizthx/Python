Algoritmo super_tienda
	Escribir 'Ingrese su Codigo: '
	Leer codigo
	Escribir 'Ingrese el nombre del producto: '
	Leer nombre
	Escribir 'Ingrese la cantidad: '
	Leer cantidad
	Escribir 'Ingrese el Valor Unitario:'
	Leer valorU
	valorsiniva = valorU * cantidad
	total = valorsiniva * 1.19
	Escribir 'El Codigo del producto es : ',codigo
	Escribir' El nombre del producto es : ' ,nombre
	Escribir' Valor del producto sin aplicar Iva: ',valorsiniva
	Escribir' Valor del producto final: ',total
FinAlgoritmo
