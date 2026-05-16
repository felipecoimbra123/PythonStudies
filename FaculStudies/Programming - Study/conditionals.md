Se algo acontece, faz uma coisa... Senão, faz outra...

Nome: Felipe Coimbra Rocha dos Santos

# Operações Relacionais
Permitem comparar dois valores através de operadores relacionais, resultando em **True** ou **False**.

### Exemplo:
```python
x > 13
```

Explicação: x > 13 será **True** se o valor da variável x for maior que 13

## Operadores Relacionais - Python
* `>` — Maior que
* `<` — Menor que
* `>=` — Maior ou igual a
* `<=` — Menor ou igual a
* `==` — Igual a
* `!=` — Diferente de

## Exercícios de Fixação

Sabendo que:
* `A = 0`
* `B = -2.5`
* `C = True`

Responda o que segue abaixo:
* 1. A > 0 - **False**
* 2. A == 0 - **True**
* 3. B <= -1 - **True**
* 4. B != 2.5 - **True**
* 5. C - **True**
* 6. A + 2 >= 3 - **False**
* 7. B + 2.5 == 0 - **True**

# Operações Lógicas
Resultam em **True** ou **False**, porém, utilizam operadores lógicos.

### Exemplo:
```python
(x > 13) and (idade + 10 == 28)
```

Explicação: Será **True** se o valor da variável x for maior que 13 **e** se o valor da variável idade com 10 for igual a 28.

## Operadores Lógicos - Python
* `not` — Negação lógica (inverte o valor da expressão)
* `and` — **e** lógico: será **True** se ambos os lados forem **True**
* `or` — **ou** lógico: será **True** se pelo menos um dos lados for **True**

## Exercícios de Fixação

Sabendo que:
* `A = 0`
* `B = -2.5`
* `C = True`

Responda o que segue abaixo:
* 1. not C - **False**
* 2. A == 0 and C - **True**
* 3. B <= -1 or A < 0 - **True**
* 4. B != 2.5 or A == 0 - **True**
* 5. C or not C - **True**
* 6. A + 2 >= 3 and B == -2.5 - **False**
* 7. B + 2.5 == 0 and C and A <= 3 - **True**

# Operação %
O operador % é chamado de MOD. Retorna o resto da divisão inteira entre dois valores.

### Exemplo:
```python
4 % 2 = 0
5 % 2 = 1
10 % 3 = 1
15 % 4 = 3
22 % 9 = 4
```
### Onde usar?
* Como saber se um valor é par ou ímpar?
* Como saber se um valor é divisível por outro?

# Instrução IF
Somente se a condição for verdadeira, os comandos serão executados.

### Sintaxe
```python
if condicao:
    comando1
    comando2
    comando3
    ...
    comandoN
```

### Exemplos
```python
if i > 7:
    print("Valor de i é maior que 7")

----------------------------

if op == 2:
    print("Opção 2")
    op = 0
    print("Opção setada para 0 de novo")

----------------------------

if A != 0 and A % 2 == 0:
    print("O valor de A é par!")
```

# Instrução IF/ELSE
Else significa senão.

### Sintaxe
```python
if condicao:
    comando1
    comando2
    comando3
    ...
    comandoN
else:
    comando1
    comando2
    comando3
    ...
    comandoN
```

### Exemplos
```python
if i > 7:
    print("Valor de i é maior que 7")
else:
    print("Valor de o é menor que 7")

----------------------------

if op == 2:
    print("Opção 2")
    op = 0
    print("Opção setada para 0 de novo")
else:
    print("Opção inválida")
    op = 2
```

# Instrução WHILE
Na instrução IF/ELSE são executados de uma vez. Aqui no WHILE, podemos repetir as mesmas instruções várias vezes. **Enquanto** uma condição for considerada **True**, os comandos vão ser realizados. Ao final dos comandos, o programa **VOLTA PARA O WHILE** pra testar a condição.

### Sintaxe
```python
while condicao:
    condicao1
    condicao2
    condicao3
    ...
    condicaoN
```

### Exemplos
```python
i = 0
while i < 7:
    print("Valor de i:", i)
    i += 1

----------------------------

op = int(input("Digite 3 para sair"))
while op != 3:
    print("\nOpção digitada:", op, "\nVocê não saiu.")
    op = int(input("Digite 3 para sair:"))
```

Existe o comando **break** que interrompe esse laço!!!!!!!!!!!!!!

### Exemplos
```python
i = 0
while i < 100:
    print("Valor de i:", i)
    i += 1
    if i == 32:
        break

----------------------------

while True:
    op = int(input("Digite 3 para sair"))
    print("\nOpção digitada:", op)
    if op == 3:
        break
    print("Você não saiu. \n")
print("\nVocê saiu.")
```

# Instrução FOR
Uma variável qualquer que vai mudar seu valor a cada iteração.

### Sintaxe
```python
for variavel in lista:
    comando1
    comando2
    comando3
    ...
    comandoN
```

### Exemplos
```python
times = ["Grêmio", "Internacional", "Barcelona"]    
for meuTime in times:
    print(meuTime)

----------------------------

numeros = [0, 1, 2, 3, 4, 5]
for i in numeros:
    print(i)

----------------------------

semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
for dia in semana:
    print(dia)
```

## Comando range
Representa uma lista de inteiros

### Exemplos
* `range(1,10) - Cria a lista [1, 2, 3, 4, 5, 6, 7, 8, 9]`
* `range(2,5) - Cria a lista [2, 3, 4]`
* `range(-6,-1) - Cria a lista [-6, -5, -4, -3, -2]`

## Como usar FOR com range?
```python
for a in range(1,10):
    print(a)

----------------------------

for b in range(2,5):
    print(b)

----------------------------

for c in range(-6,-1):
    print(c)
```

## Como criar uma lista?
Precisamos dizer que uma variável é uma lista vazia e usar o comando **append**, que adiciona um valor na lista

```python
minhaLista = [] #Criando a lista
minhaLista.append("Felipe")
minhaLista.append("Coimbra")
minhaLista.append("Rocha")
minhaLista.append("dos")
minhaLista.append("Santos")
for nome in minhaLista:
    print(nome)
```