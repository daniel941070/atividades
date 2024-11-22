#ALUNOS
#ELTON VICTOR-2024101405002
#DANIEL ALEXANDRE-20242014050028

import random

try:
    numero = random.randint(1, 100)
    nmaximo = 100
    nminimo = 1

    # Intervalo de números desejados
    minimo = 1
    maximo = 100

    # Primeira tentativa
    tentativa = 1

    # Início
    print("Tente acertar o número sorteado entre 1 e 100!")
    print("Tentativa", tentativa, ": Digite um número entre", minimo, "e", maximo, ": ")
    palpite = int(input())
    if palpite == numero:
        print("Parabéns! Você acertou o número!")
    else:
        if palpite < numero:
            print("O número sorteado é maior do que", palpite, ". Tente novamente!")
            minimo = palpite + 1
        else:
            print("O número sorteado é menor do que", palpite, ". Tente novamente!")
            maximo = palpite - 1

        # Segunda tentativa
        tentativa = 2
        print("Tentativa", tentativa, ": Digite um número entre", minimo, "e", maximo, ": ")
        palpite = int(input())
        if palpite == numero:
            print("Parabéns! Você acertou o número!")
        else:
            if palpite < numero:
                print("O número sorteado é maior do que", palpite, ". Tente novamente!")
                minimo = palpite + 1
            else:
                print("O número sorteado é menor do que", palpite, ". Tente novamente!")
                maximo = palpite - 1

            # Terceira tentativa
            tentativa = 3
            print("Tentativa", tentativa, ": Digite um número entre", minimo, "e", maximo, ": ")
            palpite = int(input())
            if palpite == numero:
                print("Parabéns! Você acertou o número!")
            else:
                if palpite < numero:
                    print("O número sorteado é maior do que", palpite, ". Tente novamente!")
                    minimo = palpite + 1
                else:
                    print("O número sorteado é menor do que", palpite, ". Tente novamente!")
                    maximo = palpite - 1

                # Quarta tentativa
                tentativa = 4
                print("Tentativa", tentativa, ": Digite um número entre", minimo, "e", maximo, ": ")
                palpite = int(input())
                if palpite == numero:
                    print("Parabéns! Você acertou o número!")
                else:
                    print("Tentativas esgotadas. Você não acertou! O número sorteado era", numero, ".")

except Exception as e:
    print("Ocorreu um erro:", e)
