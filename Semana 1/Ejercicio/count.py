cadena = 'Hoy es jueves y manana es viernes'
veces=cadena.count('jueves')
print(veces)
cadena2 = 'Hoy es jueves y manana es viernes y dentro de 8 dias es jueves'
veces2=cadena.count('jueves')
print(veces)
estado=cadena.find('word')'''cuando no encuentra en la cadena nos arroja un numero negativo'''
print(estado)
estado=cadena.rfind('dias')'''realiza la misma funcion y ubican el lugar donde se encuentra'''
print(estado)
estado=cadena.rindex('dias')'''realiza la misma funcion y ubican el lugar donde se encuentra'''
print(estado)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
cadena.startswitch('Hoy')'''el realiza la busqueda de izquierda a derecha de la palabra y arroja si es verdadero o falso'''
cadena.endswitch('Hoy')'''el realiza la busqueda de derecha a izquierda  de la palabra y arroja si es verdadero o falso'''
