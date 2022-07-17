'''

edad = ('Ingrese la edad')
estado=edad.indigit()#Verificar que solo sean digitos
print(estado)

estatura=float(input('Ingrese su estatura'))
estado2=estatura.isnumeric() #Verificar que solo sean digitos
print(estado2)

estatura=input('Ingrese su estatura')
estado3=estatura.isdecimal() #Verificar que solo sean solo digitos
print(estado3)

direccion=input('Ingrese su direccion')
print(direccion.isalnum()) #Verificar que solo sean solo numeros

direccion=input('Ingrese su direccion ')
print(direccion.isalpha()) #Verificar que solo sean solo letras

direccion=input('Ingrese su direccion ')
print(direccion.lower()) #Verificar que solo sean minusculas

direccion=input('Ingrese su direccion ')
print(direccion.upper()) #Verificar que solo sean mayuscula

texto=input('Ingrese su texto ')
print(texto.isprintable()) #Verificar que se pueda imprimir

texto=input('Ingrese su texto ')
print(texto.isspace()) #Verificar si tienes espacios

texto=input('Ingrese su texto ')
print(texto.capitalize()) #Envia la primera letra en mayuscula

texto=input('Ingrese su texto ')
texto1=input('Cual palabra reemplazar ')
texto2=input('Digite lo que desea reemplazar ')
print(texto.replace(texto1,texto2)) # Se utiliza para reemplazar

'''
