Algoritmo calculo_notas
	Escribir 'Ingrese el codigo del estudiante '
	leer codigo
	Escribir 'Ingrese nombre :'
	leer nombre
	Escribir 'Ingrese la nota 1: '
	Leer nota1
	Escribir 'Ingrese la nota 2: '
	Leer nota2
	Escribir 'Ingrese la nota 3: '
	Leer nota3
	definitiva = (nota1+nota2+nota3)/3
	Si definitiva>=3.0 Entonces
		estado='Aprobo'
	SiNo
		estado='Reprobo'
	Fin Si
	Escribir 'Codigo :',codigo,' nombre :',nombre,' obtuvo definitiva ',definitiva,' y ',estado

FinAlgoritmo
