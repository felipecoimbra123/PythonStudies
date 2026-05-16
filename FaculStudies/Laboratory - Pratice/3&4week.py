#EXERCÍCIOS IF/ELSE

# PRIMEIRO:
# - Crie um programa que recebe um inteiro pelo teclado e imprime se ele é par ou ímpar.    

a = int(input("Digite um valor numérico: "))

if a != 0 and a % 2 == 0:
    print("O valor de A é par!")
else:
    print("O valor de A é ímpar")

# SEGUNDO:
# - Crie um programa que recebe dois valores inteiros pelo teclado e imprime qual dos dois é maior.

a = int(input("Digite um valor numérico: "))
b = int(input("Digite um valor numérico: "))

if a > b:
    print("O valor", a, "é maior que", b)
elif a < b:
    print("O valor", a, "é menor que", b)
else:
    print("Os valores estão iguais")

# TERCEIRO:
# - Crie um programa que recebe dois valores inteiros A e B pelo teclado e imprime o valor de A dividido por B. Entretanto, se o valor de B for 0, imprima uma mensagem de erro e não faça a divisão

a = int(input("Digite um valor numérico: "))
b = int(input("Digite um valor numérico: "))

if b == 0:
    print("Num vai dar")
else:
    resultado = a / b
    print("o resultado da divisão é:", resultado)

# QUARTO:
# - Crie um programa que recebe três valores inteiros pelo teclado e imprime qual dos três é menor.

# QUINTO:
# - Crie um programa que recebe o preço de um produto pelo teclado e imprime na tela a mensagem adequada, de acordo com o preço:
#       • “Preço inválido”, se o preço for negativo ou zero
#       • “Preço baixo”, se o preço for entre 0 e 30 (inclusive)
#       • “Preço médio”, se o preço for entre 30 e 50 (inclusive)
#       • “Preço alto”, se o preço for maior do que 50

# SEXTO:
# -  Crie um programa que aplica uma taxa de juros em um determinado preço digitado pelo teclado. A taxa aplicada deve ser:
#        • Aumento de 10% caso o valor seja menor do que 100
#        • Aumento de 20% caso o valor esteja entre 100 (inclusive) e 300
#        • Aumento de 50% caso o valor esteja entre 300 (inclusive) e 1000
#        • Imprima uma mensagem de erro se o valor for negativo
#        • Ao final, seu programa deve imprimir o novo valor, já com a taxa aplicada.

# SÉTIMO:
# - Crie um programa que recebe um valor inteiro referente a um determinado ano. Imprima na tela se o ano informado é bissexto ou não

# OITAVO:
# - Crie um programa que exibe um menu de calculadora na tela. O menu exibido deve ser o seguinte:
#       • Digite 1 para somar dois valores
#       • Digite 2 para subtrair dois valores
#       • Digite 3 para multiplicar dois valores
#       • Digite 4 para dividir dois valores
#       • Digite 5 para realizar uma potência entre dois valores
#       • Digite 6 para realizar uma radiciação entre dois valores
#       • Digite qualquer outro número para sair
#De acordo com a opção informada pelo usuário, solicite os valores necessários para o usuário e imprima na tela o resultado da operação realizada.

# NONO:
# - Crie um programa que recebe a nota do Grau A e a nota do Grau B pelo teclado e imprime na tela se será necessário ou não realizar o Grau C (considere o sistema de avaliação da Unisinos). Caso algum valor informado seja negativo, informe uma mensagem de erro e não realize o cálculo.

# DÉCIMO:
# - Crie um programa que solicita que o usuário digite uma letra e imprime na tela se a letra é uma vogal ou uma consoante.