kmh = int(input('Digite a velocidade do carro: '))
while kmh <= 0:
    kmh = int(input('Digite uma velocidade acima de 0: '))

if kmh > 80:
    exced = kmh - 80
    multa = exced * 7
    print('Você passou do limite de 80Km/h, você será multado em {}R$'.format(multa))
else:
    print('Você está dentro do limite de 80Km/h, continue assim!')