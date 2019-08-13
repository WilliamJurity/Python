from math import radians, cos, sin, tan
ang = int(input('Digite o ângulo desejado: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tang = tan(radians(ang))

print('O seno do ângulo {} é {:.2f}'.format(ang, seno))
print('O cosseno do ângulo {} é {:.2f}'.format(ang, cosseno))
print('A tangente do ângulo {} é {:.2f}'.format(ang, tang))
