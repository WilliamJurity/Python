#Cria um dicionário
lista = dict()

while True:
    produto = input("Digite o nome do produto: ")
    while len(produto) < 2:
        print("Nome do produto não parece ser válido, tente novamente.")
        produto = input("Digite o nome do produto: ")

    valor = input("Digite o valor do produto em R$: ")
    while not valor.strip().isnumeric():
        valor = input("Digite um valor válido em R$: ")

    lista.update({produto[0]:{"valor":valor}})

    while True:
        pergunta = input("Deseja continuar? [S/N]: ")
        if pergunta.lower() == "s":
            break
        if pergunta.lower() == "n":
            break

    if pergunta == "n":
        break

soma = 0

for item in lista:
    valor = int(lista[item]["valor"])
    soma += valor


