'''from math import sqrt
print('Cauculando Hipotenusa de um triângulo')
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hp = (co ** 2 + ca ** 2)
hp = sqrt(hp)
print('O comprimento da hipotenusa é igual a: {}'.format(hp))'''

#Segunda Forma
from math import hypot
print('Cauculando Hipotenusa de um triângulo')
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hp = hypot(co, ca)
print('O comprimento da hipotenusa é igual a: {:.2f}'.format(hp))
