vlcasa = input('Digite o valor da casa: ')
while vlcasa.strip().isnumeric() == False:
    vlcasa = input('Digite um valor válido')
vlcasa = float(vlcasa)

sl = input('Digite o seu salário: ')
while sl.strip().isnumeric() == False:
    sl = input('Digite um valor válido: ')
sl = float(sl)

parcelas = input('Digite o valor das parcelas: ')
while parcelas.strip().isnumeric() == False:
    parcelas = input("Digite um valor válido: ")
parcelas = float(parcelas)

prestacao = vlcasa / parcelas
print(f"O valor de cada prestação da sua casa é {prestacao:.2f}")

x = sl * 30 / 100

if prestacao > x:
    print('Situação: NEGADO! Motivo: As prestações de {:.2f}R$ excedem 30% do seu salário mensal ({:.2f}R$).'.format(prestacao, x))
else:
    print('Situação: ACEITO!')