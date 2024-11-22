#ALUNOS
#ELTON VICTOR-2024101405002
#DANIEL ALEXANDRE-20242014050028

#Este é um programa que pergunta três valores: dia, mês e ano e responde qual dia a data corresonde.

# Solicita ao usuário o dia, mês e ano
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

# Verificar se o mês é válido
if mes < 1 or mes > 12:
    print("Mês inválido!")
else:
    # Verificar se o ano é bissexto
    bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

    # Determinar o número de dias no mês
    if mes == 1:
        dias_anteriores = 0
        dias_do_mes = 31
    elif mes == 2:
        dias_anteriores = 31
        dias_do_mes = 29 if bissexto else 28
    elif mes == 3:
        dias_anteriores = 31 + (29 if bissexto else 28)
        dias_do_mes = 31
    elif mes == 4:
        dias_anteriores = 31 + (29 if bissexto else 28) + 31
        dias_do_mes = 30
    elif mes == 5:
        dias_anteriores = 31 + (29 if bissexto else 28) + 31 + 30
        dias_do_mes = 31
    elif mes == 6:
        dias_anteriores = 31 + (29 if bissexto else 28) + 31 + 30 + 31
        dias_do_mes = 30
    elif mes == 7:
        dias_anteriores = 31 + (29 if bissexto else 28) + 31 + 30 + 31 + 30
        dias_do_mes = 31
    elif mes == 8:
        dias_anteriores = 31 + (29 if bissexto else 28) + 31 + 30 + 31 + 30 + 31
        dias_do_mes = 31
    elif mes == 9:
        dias_anteriores = 31 + (29 if bissexto else 28) + 31 + 30 + 31 + 30 + 31 + 31
        dias_do_mes = 30
    elif mes == 10:
        dias_anteriores = 31 + (29 if bissexto else 28) + 31 + 30 + 31 + 30 + 31 + 31 + 30
        dias_do_mes = 31
    elif mes == 11:
        dias_anteriores = 31 + (29 if bissexto else 28) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
        dias_do_mes = 30
    elif mes == 12:
        dias_anteriores = 31 + (29 if bissexto else 28) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
        dias_do_mes = 31

    # Verificar se o dia é válido
    if dia < 1 or dia > dias_do_mes:
        print("Dia inválido!")
    else:
        # Calcular o dia juliano
        dia_juliano = dias_anteriores + dia
        print(f"A data {dia}/{mes}/{ano} corresponde ao dia juliano {dia_juliano}.")