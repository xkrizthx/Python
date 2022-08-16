
while True:
    try:
        nombre=input('Nombre del usuario :')
        if nombre.isalpha():
            break
        else:
            print('Debe ingresar caracteres alfabéticos en el nombre')
            continue
    except ValueError:
        print('Has digitado un dato no valido como entero ...')

while True:
    try:
        estrato=int(input('Ingrese el estrato (1,2,3,4,5) :'))
        if estrato<1 or estrato>5:
            print('El valor del estrato debe ser entre (1,2,3,4 y 5) :')
            continue
        break
    except ValueError:
        print('Has digitado un dato no valido como entero ...')
if estrato ==1:
    tb=10000
elif estrato ==2:
    tb=15000
elif estrato ==3:
    tb=30000
elif estrato ==4:
    tb=50000
else:
    tb= 650000
print(f'Nombre : {nombre} ')
print("Tarifa Basica  :",'{:,.2f}'.format(tb))