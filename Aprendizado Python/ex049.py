n = input('Digite um número: ')
while not n.strip().isnumeric():
    n = input('Digite um número válido: ')

for x in range(0, 10):
    print(f"{n} X {x} = {int(n) * x}")
