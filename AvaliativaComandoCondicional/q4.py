#ALUNOS
#ELTON VICTOR-2024101405002
#DANIEL ALEXANDRE-20242014050028

# Pergunta ao usuário o ano
ano = int(input("Digite um ano: "))


if ano % 400 == 0:   #<<<<<<Verifica se o ano é divisível por 400
    print("O ano", ano, "é bissexto.") #<<<<<Se o ano for divisível por 400, ele é bissexto

# Se o ano não for divisível por 400, mas for por 4 e NÃO for por 100, ele é bissexto

else:
    if ano % 4 == 0:          #<<<<<<Verifica se o ano é divisível por 4, caso seja, verifica a seguinte questão do 100
        if ano % 100 != 0:    #<<<<<<Verifica se o ano NÃO é divisível por 100, se a divisão for diferente de 0, por exemplo 2024 dividido por 100 é igual 20.24, ou seja, tem "resto".
            print("O ano", ano, "é bissexto.")  #<<<<Se for divisível por 4 e não por 100, é bissexto
        else:
            print("O ano", ano, "não é bissexto.") #<<<<<<nesse caso se o ano for divisivel por 4 e 100 ele não é bissexto
    else:
        print("O ano", ano, "não é bissexto.")     #<<<<aqui ignora o 100, por isso esta fora do segundo if, pois caso não seja divisivel nem por 4 nem por 400 ele não é bissexto
