from random import randrange
n = int(input('Digite um número de 0 a 5 e tente advinhar: '))
while n > 5 or n < 0:
    n = int(input('Digite um número entre 0 e 5: '))

x = randrange(0, 6) #Obs: O último digite não é contado, na pratica gera um número entre 0 e 5.

if n == x:
    print('O computador escolheu {}, você ganhou! Parabéns!'.format(x))
else:
    print('O computador escolheu {}, tente novamente!'.format(x))