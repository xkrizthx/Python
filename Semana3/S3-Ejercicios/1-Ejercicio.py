while True:
    try:
        valor=int(input('Ingrese un numero :'))
        print(f'El numero ingresado es {valor}')
        break
    except ValueError:
        print('Ojo el numero ingresado no es un entero ')
print('hemos terminado la ejecución ')
        