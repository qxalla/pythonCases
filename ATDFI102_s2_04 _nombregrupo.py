#perímetro y área del triángulo con fórmula de Herón
lado_a = int(input("Ingrese la longitud del primer lado: "))
lado_b = int(input("Ingrese la longitud del segundo lado: "))
lado_c = int(input("Ingrese la longitud del tercer lado: "))
perimetro = lado_a + lado_b +lado_c
s = perimetro / 2
area=s=(s*(s-lado_a)*(s-lado_b)*(s-lado_c))**0.5
print('El área del triángulo es: %.1f cms2' %(area))
print('El perímetro del triángulo es: %.1f cms' %(perimetro))