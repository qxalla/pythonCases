#promedio de 3 numeros
suma = 0
lista_numero = ['primer', 'segundo', 'tercer']
for x in range(3):
    suma += float(input(F'Introduce el {lista_numero[x]} número: '))
print('El promedio es:', round(suma/3, 1))