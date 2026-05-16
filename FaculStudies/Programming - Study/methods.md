Nome: Felipe Coimbra Rocha dos Santos

# Métodos
É uma definição de uma determinada ação. São criados para organizar e separar ações do programa.

### Sintaxe
```python
def nomeMetodo():
    comando1
    comando2
    comando3
    ...
    comandoN
```

### Exemplo
```python
def imprimeNome():
    print("Felipe é um exemplo de método!")
```

`Porém, acima, existe um erro! Um método não faz nada sozinho sem ser chamado, então, tem que ser assim:`

```python
def imprimeNome():
    print("Felipe é um exemplo de método!")

imprimeNome() # Chamada do método
```

##  Parâmetros de entrada
São os valores que o método precisa saber para realizar a sua função.

### Exemplos
```python
def imprimeMensagem(a):
    print(a)

imprimeMensagem("Salve pra quem tá lendo!")

----------------------------

def verificaPar(a):
    if a % 2 == 0:
        print("O valor", a, "é par")
    else:
        print("O valor", a, "é impar")

verificaPar(2) # "2" vai ser o argumento passado, o que vai substituir o "a"

----------------------------

def maiorValor(a, b):
    if a > b:
        print("O valor", a, "é maior que o valor", b)
    else:
        print("O valor", b, "é maior que o valor", a)

maiorValor(-6,3)

----------------------------

def timeTorcedor(nome, time, idade):
    if time == "Inter":
        print(nome, "com essa", idade, "e ainda torce para esse time?")
    else:
        print(nome, "você já tem", idade, "anos e entende de futebol")

timeTorcedor("Felipe", "Grêmio", 18)
timeTorcedor("Bruno", "Inter", 18)
timeTorcedor("Leonardo", "Inter", 19)
``` 

##  Retorno
É o resultado que o método devolve para quem o chamou.

### Exemplos
```python
def somaValores(a, b):
    return a + b

soma = somaValores(2, 7)
print(soma)

----------------------------

def comparaValores(a, b):
    if a == b:
        return True
    else:
        return False

comparacao = comparaValores(2,2)

if comparacao:
    print("Valores iguais")
else:
    print("Valores diferentes")
``` 