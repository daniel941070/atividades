#ALUNOS
#ELTON VICTOR-2024101405002
#DANIEL ALEXANDRE-20242014050028


# Este é um programa que receba a nota de aluno do IFRN nas duas avaliações

# Receber as notas do usuário
nota_1 = float(input("Digite a nota da primeira avaliação (0 a 100): "))
nota_2 = float(input("Digite a nota da segunda avaliação (0 a 100): "))

# Verificar se as notas estão dentro do intervalo permitido
if 0 <= nota_1 <= 100 and 0 <= nota_2 <= 100:
    # Calcular a média ponderada
    media = (2 * nota_1 + 3 * nota_2) / 5

    # Verificar a situação do aluno
    if media >= 60:
        print("O aluno foi aprovado com média", round(media, 2))
    elif 20 <= media < 60:
        print("O aluno ficou de recuperação final com média", round(media, 2))
        nota_final = float(input("Digite a nota da recuperação final: "))

        # Calcular a média final (média aritmética simples)
        media_final = (media + nota_final) / 2

        # Outras opções de cálculo (média ponderada com a recuperação)
        media_final1 = (2 * nota_final + 3 * nota_2) / 5
        media_final2 = (2 * nota_1 + 3 * nota_final) / 5

        # Determinar o resultado final com base nas médias finais
        if media_final >= 60 or media_final1 >= 60 or media_final2 >= 60:
            print("O aluno foi aprovado com média", round(media_final, 2))
        else:
            print("O aluno foi reprovado com média", round(media_final, 2))
    else:
        print("O aluno foi reprovado com média", round(media, 2))
else:
    print("As notas devem estar entre 0 e 100.")