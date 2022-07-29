Algoritmo calculoparidad
	num=0
	contp=0
	conti=0
	escribir 'Ingrese numero a calcular la paridad '
	leer numero
	Mientras numero<>-1 Hacer
		residuo=numero%2
		Si residuo=0 Entonces
			contp=contp+1
		SiNo
			conti=conti+1
		Fin Si
		escribir 'Ingrese numero a calcular la paridad '
		leer numero
	Fin Mientras
	escribir 'Total de pares ',contp
	escribir 'Total de pares ',conti
FinAlgoritmo
