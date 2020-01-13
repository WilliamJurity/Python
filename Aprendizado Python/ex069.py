# Criando Dicionário
lista = dict()

while True:
    # Obtem o nome da pessoa
    pessoa = str(input("Digite o nome da pessoa: "))
    pessoa = pessoa.split()
    sexo = str(input("Qual o Sexo? [M/F]: "))
    while True:
        if sexo.lower() == "m":
            break
        elif sexo.lower() == "f":
            break
        sexo = str(input("Qual o Sexo? [M/F]: "))

    # Obtem a idade da pessoa
    idade = input("Digite a idade: ")
    while not idade.strip().isnumeric():
        idade = input("Digite uma idade válida: ")

    # Adiciona a pessoa na lista
    lista.update({pessoa[0]:{"idade":idade, "sexo":sexo}})

    # Pergunta se deseja continuar
    continuar = str(input("Deseja continuar? [S/N]: "))
    while True:
        if continuar.lower() == "n":
            break
        elif continuar.lower() == "s":
            break
        continuar = str(input("Deseja continuar? [S/N]: "))

    if continuar == "s":
        continue
    else:
        break

maioridade = []
homens = []
mulheres = []
# Separa cada pessoa em uma lista diferente
for registro in lista:
    if int(lista[registro]["idade"]) >= 18:
        maioridade.append(registro)
    if lista[registro]["sexo"].lower() == "m":
        homens.append(registro)
    if lista[registro]["sexo"].lower() == "f":
        if int(lista[registro]["idade"]) <= 20:
            mulheres.append(registro)

# Mostra o Resultado
print("Pessoas maiores de 18 anos: ")
for item in maioridade:
    print(item)

print("Homens Cadastrados: ")
for item in homens:
    print(item)

print("Mulheres com menos de 20 anos: ")
for item in mulheres:
    print(item)