ano = input('Digite o ano: ')
while ano.strip().isnumeric() == False:
    ano = input('Digite um ano válido: ')
ano = int(ano)
if ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))
elif ano % 4 == 0:
    if ano % 100 != 0:
        print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))
