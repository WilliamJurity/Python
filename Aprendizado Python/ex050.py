print('Forneça 6 números quaisquer.')
soma = 0
for c in range(1, 7):
    n = input(f"Digite o {c}º número: ")
    while not n.strip().isnumeric():
        n = input('Digite um valor válido: ')
    if int(n) % 2 == 0:
        soma += int(n)
print(f"Somando apenas os números pares, o resultado da soma foi: {soma}")