def procesar_abonado(estrato,impulsos):
    if estrato==1:
        tarifa_basica=10000
    elif estrato==2:
        tarifa_basica=15000
    elif estrato==3:
        tarifa_basica=20000
    elif estrato==4:
        tarifa_basica=25000
    else:
        tarifa_basica=30000
    consumo=impulsos*100
    valor_abonado=tarifa_basica+consumo
    return valor_abonado

def validar_estrato():
    while True:
        try:
            estrato=int(input('Estrato (1,2,3,4,5) :'))
            if estrato<1 or estrato>5:
                print('El estrato debe estar entre 1 y 5')
                continue
            break
        except ValueError:
            print('El estrato es un numero entero ')
            continue
        return estrato

def validar_decimal():
    while True:
        try:
            impulsos=float(input('Impulsos :'))
            break    
        except ValueError:
            print('El dato debe ser decimal... ')
            continue
    return impulsos

N=int(input('Cantidad de Usuarios :'))
total_abonados=0
for i in range(1,N+1):
    print('----------------')
    print(f'Lectura Abonado:{i}')
    nombre=input('Nombre :')
    #estrato=int(input('Estrato (1,2,3,4,5) :')) 
    estrato=validar_estrato()
    #impulsos=float(input('Impulsos :'))
    impulsos=validar_decimal()
       
    valor_apagar=procesar_abonado(estrato,impulsos)
    total_abonados+=valor_apagar
    print('---Salida Datos ---')
    print(f'Nombre : {nombre}')
    print(f'Estrato : {estrato}')
    print(f'Impulsos : {impulsos}')
    print(f'valor_abonado : {valor_apagar}')
print(f'Total Abonados : {total_abonados}')
     
