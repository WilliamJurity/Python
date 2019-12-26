from random import randrange

# Jogando Par ou Impar com o computador
win = 0
while True:
    # Obtem o valor digitado pelo jogador e valida.
    gamerValor = input("Digite um valor: ")
    while not gamerValor.strip().isnumeric():
        gamerValor = input("Digite um valor válido: ")
    # Obtem a escolha do jogador [PAR / IMPAR] e valida
    gamerMode = input("Par ou Ímpar? [P/I]: ")
    while True:
        if gamerMode.lower() == "p":
            break
        elif gamerMode.lower()== "i":
            break
        gamerMode = input("Par ou Ímpar? [P/I]: ")
    # Atribui um valor aleatório real entre 0 e 10 e soma com o valor digitado pelo jogador
    pcValor = randrange(0, 11)
    soma = pcValor + int(gamerValor)
    # Testa se a soma da um resultado PAR ou IMPAR e compara com a escolha do jogador
    if soma % 2 == 0:
        print(f"Você jogou {gamerValor} e o computador {pcValor}. Total de {soma} DEU PAR!")
        if gamerMode.lower() == "p":
            win += 1 # Soma quantidade de vezes que o jogador ganhou
            print("Você VENCEU!")
            print("Vamos Jogar novamente...")
        else:
            print("Você PERDEU!")
            print(f"GAME OVER! Você venceu {win} vezes." if win > 0 else "GAME OVER!")
            break
    else:
        print(f"Você jogou {gamerValor} e o computador {pcValor}. Total de {soma} DEU IMPAR!")
        if gamerMode.lower() == "i":
            win += 1 # Soma quantidade de vezes que o jogador ganhou
            print("Você VENCEU!")
            print("Vamos Jogar novamente...")
        else:
            print("Você PERDEU!")
            print(f"GAME OVER! Você venceu {win} vezes." if win > 0 else "GAME OVER!")
            break