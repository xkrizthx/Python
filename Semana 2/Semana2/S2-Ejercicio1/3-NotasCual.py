nombre=input('Ingrese nombre :')
nota_cn=int(input('Ingres nota [0-100]'))
if nota_cn<=59:
    nota_cl='D'
elif nota_cn<=79:
    nota_cl='C'
elif nota_cn<=89:
    nota_cl='B'
else:
    nota_cl='A'
print(f'Nombre :{nombre}')
print(f'Nota Cuantitativa :{nota_cn}')
print(f'Nota Cualitativa :{nota_cl}')