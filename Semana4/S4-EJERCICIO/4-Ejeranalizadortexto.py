texto=input('Ingrese texto a analizar :')
letras=[]
texto=texto.lower()  #Volver minuscula

#hola todos como estan

letras.append(input('Ingrese la primera letra :'.lower()))  # a
letras.append(input('Ingrese la segunda letra :'.lower()))  # b 
letras.append(input('Ingrese la terce letra :'.lower()))    # c

#letras = [a,b,c]

print('\n================================')
print('Cantidad de letras ')
cantidad_letras1=texto.count(letras[0])  #
cantidad_letras2=texto.count(letras[1])
cantidad_letras3=texto.count(letras[2])

print(f'Hemos encontrando  la letra: {letras[0]} esta repetida {cantidad_letras1}, veces ')
print(f'Hemos encontrando  la letra: {letras[1]} esta repetida {cantidad_letras2}, veces ')
print(f'Hemos encontrando  la letra: {letras[2]} esta repetida {cantidad_letras3}, veces ')

print('\n================================')
print('Cantidad de palabras ')
#hola todos
# 0123
palabras=texto.split()   #[hola, todos]
print(f'Hemos encontrando : {len(palabras)} palabras ')
print(palabras)

print('\n================================')
print('Letras inicio y final')
letra_inicio=texto[0]
letra_final=texto[-1]
print(f'La letra de incio es : {letra_inicio} y la letra final {letra_final} ')

