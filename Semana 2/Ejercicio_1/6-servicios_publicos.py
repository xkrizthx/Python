# Liquidacion del Servicio del Agua para N 
total_liquidacion = 0 #Acuulador
contv = 0  #Contador
conts = 0


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
    if estado == 'V':
        contv += 1 
        if estrato == 1:
            tarifa_basica =10000
        elif estrato == 2:
            tarifa_basica =20000
        elif estrato == 3:
            tarifa_basica =30000
        elif estrato == 4:
            tarifa_basica =45000
        elif estrato == 5:
            tarifa_basica =60000
        else:
            tarifa_basica =70000
        valor_consumo = consumo_mes * 200 
        total_apagar = tarifa_basica + valor_consumo
        total_liquidacion = total_liquidacion + total_apagar # Acumulador
        print('********** Liquidacion del Servicio ****************')
        print('Codigo', codigo)
        print('Nombre', nombre)        
        print('Estado', estado)
        print('Estrato', estrato)
        print('Consumo Mes :', consumo_mes)
        print('Total Apagar', total_apagar)     
       
    else:
        conts += 1  #Contador
        print('********** Liquidacion del Servicio ****************')
        print('Senor', nombre,'su servicio se encuentra suspendido por lo tanto no existe liquidacion')
    print('--------------------------------')
print('*********************************')
print('******** Estadisticas de los Datos ****************')
print('Total de liquidacion: ',total_liquidacion)
print('Total Usuarios Vigentes:', contv)
print('Total Usuarios Suspendidos:', conts)