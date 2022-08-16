from random import *
valor=randint(0,10)
'''
for i in range(10):
    valor=randint(0,10)
    print(valor)
'''    
valor2=uniform(2.0,25.0)
print(valor2)

valor3=random()
print(valor3)

lista=['lunes','Martes','Miercoles','Jueves','Viernes']
dia=choice(lista)
print(dia)

nueva_lista=[num**2 for num in range(10) if num<5]
print(nueva_lista)

opcion=int(input('Ingrese dia de la semana :'))
match opcion:
    case 1:
        print('Es lunes :')
    case 2:
        print('Es Martes :')
    case 3:
        print('Es Miercoles :')
    case 4:
        print('Es jueves :')
    case 5:
        print('Es Viernes :')
    case _:
        print('Dia no laboral')
        
        
        