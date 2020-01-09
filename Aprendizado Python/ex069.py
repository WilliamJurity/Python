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

for pessoa in lista:
    if i["idade"] >= 18:
        maioridade.append(pessoa)
    elif i["sexo"].lower() == "m":
        homens.append(pessoa)
    elif i["sexo"].lower() == "f":
        mulheres.append(pessoa)
