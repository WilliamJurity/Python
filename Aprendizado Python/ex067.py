# Mostrando a Tabuada

while True:
    num = input("Quer ver a tabuada de qual valor? ")
    while not num.strip().isnumeric():
        num = input("Digite um valor válido: ")
    if num == "999":
        break
    for count in range(1, 11):
        soma = int(num) * count
        print(f'{num} X {count} = {soma}')