km = int(input('Digite quantos quilometros terá sua viagem: '))

while km <= 0:
    km = int(input('Digite uma quilometragem válida: '))

if km >= 200:
    preco = 0.45 * km
    print('Sua viagem irá custar 0.45/hm, dando {:.2f}R$'.format(preco))
else:
    preco = 0.50 * km
    print('Sua viagem irá custar 0.50/km, dando {:.2f}R$'.format(preco))
