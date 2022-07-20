'''
Lea una cadena de caracteres por teclado
y ademas a partir de la lectura de un caracter identifique el indice
y partir del indice extraiga todos datos hacia adelante

Hola todos como estan
0123
a->indice 3
Extraiga 'a todos como estan'

'''
cadena=input('Ingrese cadena a analizar ')
letra=input('Ingrese caracter de busqueda ')
indice=cadena.index(letra)
print(indice)
print(cadena[indice::2])
