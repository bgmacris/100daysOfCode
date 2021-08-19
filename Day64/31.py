'''
*Acumulado*
Listar los números entre 1 y 10. En la columna contigua sus cuadrados, y en la tercera columna sus cubos.
Al final dar la suma de todos los valores de cada columna.
'''

s1=s2=s3=0
for i in range(1,11):
    x = [5-len(str(i)), 5-len(str(i**2))]
    s1 += i 
    s2 += i**2
    s3 += i**3
    print(f'{i}' + ' '*x[0] + f'{i**2}' + ' '*x[1] + f'{i**3}')

print('-'*17)
x = [5-len(str(s1)), 5-len(str(s2))]
print(f'{s1}' + ' '*x[0] + f'{s2}' + ' '*x[1] + f'{s3}')
