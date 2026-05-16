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

a = int(input("Digite um valor numérico: "))
b = int(input("Digite um valor numérico: "))
c = int(input("Digite um valor numérico: "))

if a <= b and a <= c:
    print("O menor valor é ", a)
elif b <= a and b <=c:
    print("O menor valor é", b)
else:
    print("O menor valor é", c)

# QUINTO:
# - Crie um programa que recebe o preço de um produto pelo teclado e imprime na tela a mensagem adequada, de acordo com o preço:
#       • “Preço inválido”, se o preço for negativo ou zero
#       • “Preço baixo”, se o preço for entre 0 e 30 (inclusive)
#       • “Preço médio”, se o preço for entre 30 e 50 (inclusive)
#       • “Preço alto”, se o preço for maior do que 50

a = float(input("Digite o preço do produto: "))

if a <= 0:
    print("Preço inválido")
elif a >= 0 and a <= 30:
    print("Preço baixo")
elif a >= 30 and a <= 50:
    print("Preço médio")
elif a > 50:
    print("Preço alto")

# SEXTO:
# -  Crie um programa que aplica uma taxa de juros em um determinado preço digitado pelo teclado. A taxa aplicada deve ser:
#        • Aumento de 10% caso o valor seja menor do que 100
#        • Aumento de 20% caso o valor esteja entre 100 (inclusive) e 300
#        • Aumento de 50% caso o valor esteja entre 300 (inclusive) e 1000
#        • Imprima uma mensagem de erro se o valor for negativo
#        • Ao final, seu programa deve imprimir o novo valor, já com a taxa aplicada.

a = float(input("Digite o preço do produto: "))

if a < 0:
    print("Valor negativo")
elif a < 100:
    print("Aumento de 10%:", a * 1.10)
elif a >= 100 and a < 300:
    print("Aumento de 20%:", a * 1.20)
elif a >= 300 and a <= 1000:
    print("Aumento de 50%:", a * 1.50)

# SÉTIMO:
# - Crie um programa que recebe um valor inteiro referente a um determinado ano. Imprima na tela se o ano informado é bissexto ou não

a = int(input("Digite um ano: "))

if a % 4 == 0:
    print("O ano", a, "é bissexto")
else:
    print("O ano", a, "não é bissexto")

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

print("Digite 1 para somar dois valores")
print("Digite 2 para subtrair dois valores")
print("Digite 3 para multiplicar dois valores")
print("Digite 4 para dividir dois valores")
print("Digite 5 para realizar uma potência entre dois valores")
print("Digite 6 para realizar uma rediciação entre dois valores")
print("Digite qualquer outro número para sair")

opcao = int(input("Digite a opção escolhida: "))

a = int(input("Digite um valor numérico: "))
b = int(input("Digite um valor numérico: "))

if opcao == 1:
    print("Soma dos valores: ", (a + b))
elif opcao == 2:
    print("Diferença dos valores: ", (a - b))
elif opcao == 3:
    print("Produto dos valores: ", (a * b))
elif opcao == 4:
    if b != 0:
        print("Divisão dos valores: ", (a / b))
    else:
        print("Não posso dividir por 0")
elif opcao == 5:
    print("'a' elevado a 'b': ", (a ** b))
elif opcao == 6:
    print("Raiz (fator b) de a: ", (a**(1/b)))
else:
    print("Valeu falou")


# NONO:
# - Crie um programa que recebe a nota do Grau A e a nota do Grau B pelo teclado e imprime na tela se será necessário ou não realizar o Grau C (considere o sistema de avaliação da Unisinos). Caso algum valor informado seja negativo, informe uma mensagem de erro e não realize o cálculo.

grauA = float(input("Qual sua nota no Grau A? "))
grauB = float(input("Qual sua nota no Grau B? "))

if grauA >= 0 and grauB >= 0:
    notaFinal = grauA * 0.33 + grauB * 0.67
    if notaFinal >= 6:
        print("Você não precisa fazer o Grau C, nota:", notaFinal)
    else:
        print("Precisa fazer a prova de Grau C, nota:", notaFinal)
else:
    print("Já que umas das notas é negativa, não conseguimos realizar o cálculo.")

# DÉCIMO:
# - Crie um programa que solicita que o usuário digite uma letra e imprime na tela se a letra é uma vogal ou uma consoante.

letra = input("Digite uma letra: ")

if letra == "A" or letra == "a" or letra == "E" or letra == "e" or letra == "I" or letra == "i" or letra == "O" or letra == "o" or letra == "U" or letra == "u":
    print("Sua letra é uma vogal")
else:
    print("Sua letra é uma consoante")