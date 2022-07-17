Algoritmo calculo_imc
	Escribir 'Escriba la Cedula'
	Leer cedula
	Escribir 'Digite su  nombre'
	Leer nombre
	Escribir 'Digite su  Peso'
	Leer peso
	Escribir 'Digite su  estatura'
	Leer estatura
	imc <- peso/(estatura*estatura)
	Si imc<=20 Entonces
		estado <- 'Delgado'
	SiNo
		Si imc<=25 Entonces
			estado <- 'Normal de Peso'
		SiNo
			estado <- 'Sobre Peso'
		FinSi
	FinSi
	Escribir 'cedula ',cedula,' nombre ',nombre
	Escribir 'Usted se encuentra en estado: ',estado,' y su imc: ',imc
FinAlgoritmo
