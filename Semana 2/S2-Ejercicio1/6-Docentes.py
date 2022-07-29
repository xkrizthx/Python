contA=0
contB=0
contC=0
nomina_total=0
N=int(input('Ingrese numero de docentes :'))
for i in range(1,N+1):
    #print('-----------------------')
    print(f'Datos Docente {i}')
    documento=input(f'Documento :')
    nombre=input(f'Nombre :').upper()
    horas_laboradas=int(input('Horas Laboradas :'))
    categoria=input(f'Categoria (A,B,C) :').upper()
    bandera=0
    while (bandera!=-1):
        if (categoria=='A' or categoria=='B' or categoria=='C'):
            if categoria=='A':
                honorarios=horas_laboradas*25000
                contA+=1
            elif categoria=='B':
                honorarios=horas_laboradas*35000
                contB+=1
            else: 
                honorarios=horas_laboradas*50000
                contC+=1
            bandera=-1
        else:           
            print('Has cometido un error debes ingresar categoria A,B,C')
            categoria=input(f'Categoria (A,B,C) :').upper()
            bandera=0
                
    nomina_total=nomina_total+honorarios
    print('-----------------------')
    print(f'Datos docente {i}')
    print(f'nombre: {nombre}')
    print(f'categoria: {categoria}')
    print(f'Horas Laboradas: {horas_laboradas}')
    print(f'Honorarios : {honorarios}')
    print('-----------------------')
    
print('************************')
print(' Estadistica de Cierre ')
print(f'Total docentes categoria A:{contA}')
print(f'Total docentes categoria B:{contB}')
print(f'Total docentes categoria C:{contC}')
print(f'Nomina Total:{nomina_total}')

