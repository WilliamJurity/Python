sl = input('Digite seu salário: ')
while sl.strip().isnumeric() == False:
    sl = input('Digite um valor válido: ')

sl = float(sl)

if sl > 1250.00:
    print('Você tem direito a 10% de aumento. Seu novo salário é: {}'.format(sl + sl * 10 / 100))
else:
    print('Você tem direito a 15% de aumento. Seu novo salário é: {}'.format(sl + sl * 15 / 100))
