#ALUNOS
#ELTON VICTOR-2024101405002
#DANIEL ALEXANDRE-20242014050028

peso = float(input("Digite o peso em kg: ")) #solicita o peso do usuario
altura = float(input("Digite a altura em cm: ")) / 100  # Altura informada em cm e convertida para metros
imc = round(peso / (altura ** 2), 1)  # Cálculo do IMC e arredondado para 1 casa decimal
print("O IMC é:", imc)

if imc <= 18.5: #usando condicionais, mostra com base o imc, a situação do usuário
    print("ABAIXO DO PESO: Procure um médico. Algumas pessoas têm um baixo peso por características do seu organismo e tudo bem. Outras podem estar enfrentando problemas, como a desnutrição. É preciso saber qual é o caso.")
elif 18.6 <= imc < 24.9:
    print("PESO NORMAL: Que bom que você está com o peso normal! E o melhor jeito de continuar assim é mantendo um estilo de vida ativo e uma alimentação equilibrada.")
elif 25.0 <= imc < 29.9:
    print("SOBREPESO: Ele é, na verdade, uma pré-obesidade e muitas pessoas nessa faixa já apresentam doenças associadas, como diabetes e hipertensão. Importante rever hábitos e buscar ajuda antes de, por uma série de fatores, entrar na faixa da obesidade pra valer.")
elif 30.0 <= imc < 34.9:
    print("OBESIDADE GRAU I: Sinal de alerta! Chegou na hora de se cuidar, mesmo que seus exames sejam normais. Vamos dar início a mudanças hoje! Cuide de sua alimentação. Você precisa iniciar um acompanhamento com nutricionista e/ou endocrinologista.")
elif 35.0 <= imc < 39.9:
    print("OBESIDADE GRAU II: Mesmo que seus exames aparentem estar normais, é hora de se cuidar, iniciando mudanças no estilo de vida com o acompanhamento próximo de profissionais de saúde.")
elif imc >= 40.0:
    print("OBESIDADE GRAU III: Aqui o sinal é vermelho, com forte probabilidade de já existirem doenças muito graves associadas. O tratamento deve ser ainda mais urgente.")
