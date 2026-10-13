"""
FORTALECIDA NO PYTHON — Fundamentos de Python
Arquivo de revisão com exemplos simples e executáveis.

Tópicos: strings, variáveis, conversão de tipos, entrada e saída,
operadores, condicionais, laços, listas, tuplas, conjuntos,
dicionários, funções, exceções e módulos.
"""

import math
import random


def estudar_strings():
    print("\n=== STRINGS ===")
    nome = "Luffy"
    texto = "Python"

    print(nome.upper())
    print(nome.lower())
    print(nome.replace("Luffy", "Zoro"))
    print("Quantidade de caracteres:", len(nome))
    print(texto.startswith("Py"))
    print(texto.endswith("on"))
    print("Posição de 'th':", texto.find("th"))
    print("Dividindo texto:", texto.split("t"))

    print("Primeiro caractere:", nome[0])
    print("Parte da string:", nome[1:4])
    print("Três primeiros:", nome[:3])
    print("Do terceiro em diante:", nome[2:])
    print("String invertida:", nome[::-1])


def estudar_variaveis_e_tipos():
    print("\n=== VARIÁVEIS E TIPOS ===")
    nomes = ["Luffy", "Zoro", "Nami"]
    numeros = [1, 2, 3]
    lista_vazia = []

    nome = "Luffy"
    idade = 19
    peso = 65.0

    print("Nome:", nome)
    print(f"{nome} tem {idade} anos.")
    print("Peso:", peso)
    print("Listas:", nomes, numeros, lista_vazia)

    numero_texto = "10"
    print(int(numero_texto))
    print(float(numero_texto))
    print(str(10))

    print(type(10))
    print(type(3.14))
    print(type("Python"))
    print(type(True))
    print(isinstance(10, int))
    print(isinstance("Python", str))


def estudar_operadores():
    print("\n=== OPERADORES ===")
    soma = 1 + 1
    subtracao = 1 - 1
    multiplicacao = 2 * 1
    divisao = 2 / 1
    potencia = 2 ** 3
    resto = 10 % 3

    print("Soma:", soma)
    print("Subtração:", subtracao)
    print("Multiplicação:", multiplicacao)
    print("Divisão:", divisao)
    print("Potência:", potencia)
    print("Resto:", resto)

    print(10 > 5)
    print(10 < 5)
    print(10 >= 5)
    print(10 <= 5)
    print(10 == 5)
    print(10 != 5)

    print(True and False)
    print(True or False)
    print(not True)


def estudar_condicionais():
    print("\n=== CONDICIONAIS ===")
    salario = 3500

    if salario <= 0:
        classificacao = "Salário não informado ou inválido"
    elif salario < 3000:
        classificacao = "Programador júnior"
    elif salario < 7000:
        classificacao = "Programador pleno"
    else:
        classificacao = "Programador sênior"

    print(f"Salário de R$ {salario:.2f}: {classificacao}")


def estudar_lacos():
    print("\n=== LAÇOS DE REPETIÇÃO ===")
    print("Contagem de 1 a 10:")
    for numero in range(1, 11):
        print(numero, end=" ")
    print()

    frutas = ["Maçã", "Banana", "Uva"]
    for fruta in frutas:
        print(fruta)

    print("Exemplo de break:")
    for numero in range(10):
        if numero == 5:
            break
        print(numero, end=" ")
    print()

    print("Exemplo de continue:")
    for numero in range(10):
        if numero == 5:
            continue
        print(numero, end=" ")
    print()

    contador = 1
    while contador <= 5:
        print(contador, end=" ")
        contador += 1
    print()

    for indice, fruta in enumerate(frutas, start=1):
        print(indice, fruta)


def estudar_colecoes():
    print("\n=== TUPLAS, CONJUNTOS E LISTAS ===")
    cores = ("Azul", "Verde", "Vermelho")
    print("Primeira cor:", cores[0])

    numeros = {1, 2, 3, 3, 2, 1}
    print("Conjunto sem duplicatas:", numeros)

    nomes = ["Luffy", "Zoro", "Nami"]
    print("Primeiro nome:", nomes[0])
    nomes[0] = "Sanji"
    print("Lista atualizada:", nomes)

    numeros_lista = [1, 2, 3]
    numeros_lista[0] = 10
    print("Quantidade:", len(numeros_lista))
    print("Menor valor:", min(numeros_lista))
    print("Maior valor:", max(numeros_lista))

    personagens = []
    personagens.append("Sanji")
    personagens.append("Chopper")
    personagens.append("Robin")
    personagens.insert(1, "Usopp")
    print("Lista após adicionar:", personagens)

    if "Luffy" in nomes:
        print("Luffy está na lista.")
    else:
        print("Luffy não está na lista.")

    personagens.remove("Chopper")
    ultimo = personagens.pop()
    primeiro = personagens.pop(0)
    print("Elemento removido do fim:", ultimo)
    print("Elemento removido do início:", primeiro)

    personagens.sort()
    personagens.reverse()
    print("Lista ordenada e invertida:", personagens)

    if "Usopp" in personagens:
        print("Índice de Usopp:", personagens.index("Usopp"))
    print("Ocorrências de Usopp:", personagens.count("Usopp"))
    print("Tamanho da lista:", len(personagens))

    valores_logicos = [False, False, True]
    print("Existe algum valor verdadeiro?", any(valores_logicos))

    quadrados = [numero ** 2 for numero in range(10)]
    print("Quadrados:", quadrados)


def estudar_dicionarios():
    print("\n=== DICIONÁRIOS ===")
    personagem = {"nome": "Luffy", "idade": 19, "peso": 65.0}
    print("Nome:", personagem["nome"])

    for chave, valor in personagem.items():
        print(chave, valor)

    print("Chaves:", list(personagem.keys()))


def estudar_funcoes():
    print("\n=== FUNÇÕES ===")

    def somar(valor1, valor2):
        """Retorna a soma de dois valores."""
        return valor1 + valor2

    def saudacao(nome="Visitante"):
        print(f"Olá, {nome}!")

    print("Resultado:", somar(10, 20))
    saudacao()
    saudacao("Luís")

    def registrar(nome, idade):
        print(f"Nome: {nome}; idade: {idade}")

    registrar(idade=20, nome="Luís")


def estudar_excecoes_e_funcoes_embutidas():
    print("\n=== EXCEÇÕES E FUNÇÕES EMBUTIDAS ===")
    texto_idade = "vinte"

    try:
        idade = int(texto_idade)
        print("Idade:", idade)
    except ValueError:
        print(f"Não foi possível converter {texto_idade!r} para um número inteiro.")

    print("Valor absoluto:", abs(-10))
    print("Arredondamento:", round(3.14159, 2))
    print("Soma:", sum([1, 2, 3]))
    print("Maior:", max([5, 8, 2]))
    print("Menor:", min([5, 8, 2]))


def estudar_modulos():
    print("\n=== MÓDULOS ===")
    print("Raiz quadrada de 25:", math.sqrt(25))
    print("Número aleatório entre 1 e 10:", random.randint(1, 10))


def main():
    """Executa os exemplos em sequência."""
    estudar_strings()
    estudar_variaveis_e_tipos()
    estudar_operadores()
    estudar_condicionais()
    estudar_lacos()
    estudar_colecoes()
    estudar_dicionarios()
    estudar_funcoes()
    estudar_excecoes_e_funcoes_embutidas()
    estudar_modulos()


if __name__ == "__main__":
    main()
