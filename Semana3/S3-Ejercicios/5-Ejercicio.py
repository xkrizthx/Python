'''
nombre=input('Ingrese nombre completo :')
cadena=nombre.split()
print('Primer nombre ',cadena[0])
print('Segundo nombre ',cadena[1])
'''
def suma(numero1, numero2):
    sumar=numero1+numero2
    return sumar

numero1=int(input('Ingrese primer Numero :'))
numero2=int(input('Ingrese segundo Numero :'))
totalizar=suma(numero1,numero2)   #<--Retorna
print(totalizar)


totalizar2=suma(2,5)
print(totalizar2)



