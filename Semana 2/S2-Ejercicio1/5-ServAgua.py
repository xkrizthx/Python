# Liquidacion del Servicio del Agua para N 
# Realizar La siguiente adecuación:
# Al final Imprimir el total_liguidacion de todos los clientes.
# Cuente Cuantos Usuarios tienen el servicio Suspendio y Cuantos Vigentes

total_liguidacion=0   #Acumulador
contv=0  #Contador
conts=0

n=int(input('Ingrese numero de Usuarios a Calcular Liquidacion del servicio :'))
print('--------------------------------')
for i in range(1,n+1):
    print(f'Ingres datos del Usuario:[{i}] ')
    codigo=int(input(f'Ingrese codigo :'))
    nombre=input(f'Nombre :')
    estado=input(f'Estado [V=Vigente, S=Suspendido] :')
    estrato=int(input(f'Estrato [1,2,3,4,5,6] :'))
    consumo_mes=float(input(f'Consumo mes(cm3) :'))
    print('--------------------------------')
    if estado=='V':
        contv+=1
        #contv=contv+1
        if estrato==1:
            tarifa_basica=10000
        elif estrato==2:
            tarifa_basica=20000
        elif estrato==3:
            tarifa_basica=30000
        elif estrato==4:
            tarifa_basica=45000
        elif estrato==5:
            tarifa_basica=60000
        else:
            tarifa_basica=70000
        valor_consumo=consumo_mes*200
        total_pagar=tarifa_basica+valor_consumo 
        total_liguidacion=total_liguidacion+total_pagar  #Acumulador
        print('*** Liquidacion del Servicio **') 
        print(f'Nombre :{nombre}')
        print(f'Codigo :{codigo}') 
        print(f'Estado :{estado}')
        print(f'Estrato :{estrato}')
        print(f'Total a Pagar :{total_pagar}')
        print('--------------------------------')
    else:
        conts+=1  #Contador
        print('*** Liquidacion del Servicio **') 
        print(f'Señor {nombre}, su servicio se encuentra suspendido por lo tanto no se liquida')
        print('--------------------------------')
print('********************************')
print('***Estadistica de los datos***')
print(f'Total liquidacion :{total_liguidacion}')
print(f'Total Usuarios Vigentes :{contv}')
print(f'Total Usuarios Suspendidos :{conts}')
'''
1025 Juan Perez Estado:V Estrato:1 Consumo: 200
1026 Maria Luna Estado:S Estrato:1 Consumo: 100
1027 Jorge Gomez Estado:V Estrato:4 Consumo: 100
1027 Jorge Gomez Estado:V Estrato:5 Consumo: 50

'''