nombre= input('Ingrese su nombre: ')
nota_cn=int(input('Ingrese su nota: '))
if nota_cn<=59:
    nota_cl='D'
elif nota_cn<=79:
    nota_cl='C'
elif nota_cn<=89:
    nota_cl='B'
else:
    nota_cl='A'
print('Nombre ',nombre)
print('Nota Cuantitativa ',nota_cn)
print('Nota Cualitativa ',nota_cl)