#VARIÁVEIS
idade = 18 #Variável idade que recebe o valor "18" (int)
x = "Até a pé nós iremos..." #Variável x que recebe o valor "teste" (string)

#PRINTAR
print(x) #Mostrando a informação que estiver dentro da variável 
print("Até a pé nós iremos...", idade) #Mostrando a string que estiver dentro e o valor de 'idade'

#ENTRADA DE DADOS
nome = input("Digite o nome: ")
print("Seu nome é:", nome)

altura = input("Digite sua altura: ") #Input sempre entra como texto (string)
print("Sua altura é:", altura)

preco = float(input("Digite o preço: ")) #Convertendo o valor para float, poderia ser usado int também
print("O preço é:", preco)

#PROGRAMAS PRÁTICOS
precoItem1 = float(input("Digite o preço do item 1: "))
precoItem2 = float(input("Digite o preço do item 2: "))

print("O preço total é:", precoItem1 + precoItem2)

precoItem3 = float(input("Digite o preço do item 3: "))
desconto = precoItem3 * 0.1

print("Preço normal:", precoItem3)
print("Preço do desconto:", desconto)
print("Preço com desconto aplicado:", precoItem3 - desconto)

valor = float(input("Digite o valor 1: "))
valor2 = float(input("Digite o valor 2: "))
valor3 = float(input("Digite o valor 3: "))

media = (valor + valor2 + valor3) / 3

print("A média dos valores é:", media)

#EXERCÍCIOS

# PRIMEIRO:
# - Solicitar o nome do usuário
# - Usuário insere seu nome
# - Imprime nome do usuário na tela

nomeUsuario = input("Digite seu nome: ")

print("Seu nome é:", nomeUsuario)

# SEGUNDO:
# - Solicitar o nome do usuário
# - Usuário insere seu nome
# - Solicitar a idade do usuário
# - Usuário insere sua idade
# - Imprime nome e idade do usuário na tela

nomeUsuario2 = input("Digite seu nome: ")
idadeUsuario = int(input("Digite sua idade: "))

print("Seu nome é:", nomeUsuario2,)
print("Sua idade é:", idadeUsuario)

# TERCEIRO:
# - Solicitar o nome do usuário
# - Usuário insere seu nome
# - Imprime nome de usuário na tela
# - Solicitar a altura do usuário
# - Usuário insere sua altura
# - Imprime altura de usuário na tela
# - Imprime mensagem de agradecimento

nomeUsuario3 = input("Digite seu nome: ")
alturaUsuario = float(input("Digite sua altura: "))

print("Seu nome é:", nomeUsuario3,)
print("Sua altura é:", alturaUsuario,)
print("OBRIGADO POR ESCOLHER NOSSO SERVIÇO!")

# QUARTO:
# - Crie um programa que solicita informações completas do endereço do usuário (como nome da rua, cep, bairro etc.). Depois disto, seu programa deve imprimir na tela as informação do endereço do usuário de forma clara e organizada

nomeRua = input("Digite a sua rua: ")
cep = input("Digite seu cep: ")
bairro = input("Digite seu bairro: ")

print(f"Você mora na rua {nomeRua}, no cep {cep}, lozalizado no bairro {bairro}.")

#QUINTO
# - Crie um programa que pede 5 números inteiros pelo teclado e imprime as seguintes informações:
#       A soma de todos os números
#       O produto de todos os números

numero1 = int(input("Digite um número aleatório: "))
numero2 = int(input("Digite um número aleatório: "))
numero3 = int(input("Digite um número aleatório: "))
numero4 = int(input("Digite um número aleatório: "))
numero5 = int(input("Digite um número aleatório: "))

print("A soma dos números é:", numero1 + numero2 + numero3 + numero4 + numero5)
print("A multiplicação dos números é:", numero1 * numero2 * numero3 * numero4 * numero5)

#SEXTO
# - Crie um programa que pede 5 números inteiros pelo teclado e armazena-os, respectivamente, nas variáveis A, B, C, D e E. Em seguida, faça o que se pede:
#       sabendo que B e C são respectivamente a base e a altura de um triângulo, imprima a área deste triângulo
#       sabendo que A, B, C e D formam um retâgulo, imprima o perímetro deste retângulo
#       sabendo que E é o valor do raio de um determinado círculo, imprima a área deste círculo

A = int(input("Digite o valor A: "))
B = int(input("Digite o valor B: "))
C = int(input("Digite o valor C: "))
D = int(input("Digite o valor D: "))
E = int(input("Digite o valor E: "))

print("A área do triângulo, calculada pelos valores B e C (Base a altura), é:", B * C / 2)
print("O perímetro do retângulo, calculado pelos valores A, B, C e D, é:", A + B + C + D)
print("A área do círculo, calculado pelo valor de E, é:", 3.14 * (E ** 2)) # ** significa elevado (potência)

#SÉTIMO
# Uma determinada disciplina possui apenas 3 avaliações: o trabalho (que vale 10% da nota), a prova (que vale 60% da nota) e o teste (que vale 30% da nota).
# - Crie um programa que pede para o usuário digitar as notas que ele tirou nestas avaliações e imprime na tela a nota final do aluno.

trabalho = float(input("Qual sua nota no trabalho? "))
prova = float(input("Qual sua nota da prova? "))
teste = float(input("Qual sua nota no teste? "))

notaFinal = (trabalho * 0.10) + (prova * 0.60) + (teste * 0.30) # 0.10, 0.60 e 0.30 equivalem a porcentagem que cada atividade vale.

print("Sua nota final foi:", notaFinal)

#OITAVO
# Uma disciplina possui Grau A e Grau B. A nota de Grau A vale 33% da nota final, enquanto a nota do Grau B vale 67% da nota final. O Grau A possui as seguintes avaliações:
#       Atividade prática: 45% da nota do Grau A
#       Atividade teórica: 55% da nota do Grau A
# Já o Grau B possui as seguintes avaliações:
#       Prova em laboratório: 60% da nota do grau B
#       Teste teórico: 20% da nota do Grau B
#       Trabalho extraclasse: 20% da nota do Grau B
# Crie um programa que solicite as notas de todas as avaliações e imprime na tela a nota final obtido em cada disciplina.

notaPratica = float(input("Qual sua nota na atividade prática? (Grau A) "))
notaTeorica = float(input("Qual sua nota na atividade teórica? (Grau A) "))

notaLaboratorio = float(input("Qual sua nota na prova em laboratório? (Grau B) "))
notaTeste = float(input("Qual sua nota na atividade prática? (Grau B) "))
notaExtra = float(input("Qual sua nota na atividade prática? (Grau B) "))

notaFinalGrauA = (notaPratica * 0.45) + (notaTeorica * 0.55)
notaFinalGrauB = (notaLaboratorio * 0.60) + (notaTeste * 0.20) + (notaExtra * 0.20)

print("Sua nota no Grau A:", notaFinalGrauA)
print("Sua nota no Grau B:", notaFinalGrauB)

print("Sua nota final da disciplina:", (notaFinalGrauA * 0.33) + (notaFinalGrauB * 0.67))