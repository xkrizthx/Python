#Crear una función para validar que el numero leido sea entero Excepciones
#Elevar a la potencia de 2, --> retorna la potenciación
# numero**2

def potencia(etiqueta):
    while True:
        try:
            valor=int(input(etiqueta))
            cuadrado=valor**2
            break
        except ValueError:
            print('Ojo el numero ingresado no es un entero ')
    return cuadrado

valor=potencia('Ingrese un número ')
print(f'La potencia es igual a {valor}')