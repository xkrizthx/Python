#Vamos a validar categorias 1,2 o 3 que sean enteros.
while True:
    try:
        categoria=int(input('Ingrese la categoria (1,2,3) :'))
        if categoria<1 or categoria>3:
            print('El valor de la categoria debe ser entre (1,2,3) :')
            continue
        break
    except ValueError:
        print('Has digitado un dato no valido como entero ...')
print(f'El Usuario digito la categoria : {categoria}')
