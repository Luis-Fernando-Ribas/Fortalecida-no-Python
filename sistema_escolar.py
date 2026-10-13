"""
FORTALECIDA NO PYTHON — Sistema Escolar
Exercício de prática com listas, dicionários, funções, laços e validação.
"""

import os


NOTA_MINIMA_APROVACAO = 7.0
NOTA_MINIMA = 0.0
NOTA_MAXIMA = 10.0


def limpar_terminal():
    """Limpa o terminal em Windows, Linux ou macOS."""
    comando = "cls" if os.name == "nt" else "clear"
    # Em terminais sem suporte ao comando, o programa continua funcionando.
    if os.system(comando) != 0:
        print("\n" * 3)


def ler_inteiro(mensagem, minimo=None, maximo=None):
    """Lê um número inteiro, repetindo até receber um valor válido."""
    while True:
        try:
            valor = int(input(mensagem))
            if minimo is not None and valor < minimo:
                print(f"Digite um número maior ou igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Digite um número menor ou igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def ler_nota(mensagem):
    """Lê uma nota entre 0 e 10."""
    while True:
        try:
            nota = float(input(mensagem).replace(",", "."))
            if NOTA_MINIMA <= nota <= NOTA_MAXIMA:
                return nota
            print(f"A nota deve estar entre {NOTA_MINIMA:.0f} e {NOTA_MAXIMA:.0f}.")
        except ValueError:
            print("Entrada inválida. Digite uma nota, por exemplo 7.5.")


def calcular_situacao(media):
    """Retorna a situação do aluno com base na média."""
    if media >= NOTA_MINIMA_APROVACAO:
        return "Aprovado"
    return "Reprovado"


def cadastrar_aluno(alunos):
    """Solicita os dados e adiciona um aluno à lista."""
    print("\n--- Cadastro de aluno ---")
    nome = input("Nome do aluno: ").strip()

    while not nome:
        print("O nome não pode ficar vazio.")
        nome = input("Nome do aluno: ").strip()

    idade = ler_inteiro("Idade do aluno: ", minimo=0, maximo=120)
    nota1 = ler_nota("Nota 1 (0 a 10): ")
    nota2 = ler_nota("Nota 2 (0 a 10): ")

    media = (nota1 + nota2) / 2
    aluno = {
        "nome": nome,
        "idade": idade,
        "nota1": nota1,
        "nota2": nota2,
        "media": media,
        "situacao": calcular_situacao(media),
    }

    alunos.append(aluno)
    print(f"\nAluno(a) {nome} cadastrado(a) com sucesso!")
    pausar()


def exibir_aluno(aluno):
    """Mostra os dados de um aluno de forma padronizada."""
    print("\n--- Dados do aluno ---")
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Nota 1: {aluno['nota1']:.2f}")
    print(f"Nota 2: {aluno['nota2']:.2f}")
    print(f"Média: {aluno['media']:.2f}")
    print(f"Situação: {aluno['situacao']}")


def listar_alunos(alunos):
    """Lista os alunos cadastrados."""
    print("\n--- Lista de alunos ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for indice, aluno in enumerate(alunos, start=1):
            print(f"\nAluno #{indice}")
            exibir_aluno(aluno)
    pausar()


def buscar_aluno(alunos):
    """Busca alunos pelo nome, ignorando maiúsculas e minúsculas."""
    print("\n--- Buscar aluno ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        pausar()
        return

    busca = input("Digite o nome (ou parte do nome) do aluno: ").strip().casefold()
    if not busca:
        print("A busca não pode ficar vazia.")
        pausar()
        return

    encontrados = [
        aluno for aluno in alunos
        if busca in aluno["nome"].casefold()
    ]

    if encontrados:
        for aluno in encontrados:
            exibir_aluno(aluno)
    else:
        print("Nenhum aluno encontrado com esse nome.")

    pausar()


def mostrar_media_turma(alunos):
    """Calcula a média das médias dos alunos cadastrados."""
    print("\n--- Média da turma ---")
    if not alunos:
        print("Não há alunos cadastrados.")
    else:
        media_turma = sum(aluno["media"] for aluno in alunos) / len(alunos)
        aprovados = sum(
            1 for aluno in alunos
            if aluno["situacao"] == "Aprovado"
        )
        print(f"Quantidade de alunos: {len(alunos)}")
        print(f"Média geral da turma: {media_turma:.2f}")
        print(f"Aprovados: {aprovados}")
        print(f"Reprovados: {len(alunos) - aprovados}")
    pausar()


def pausar():
    input("\nPressione ENTER para continuar...")


def mostrar_menu():
    print("======= SISTEMA ESCOLAR =======")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("4 - Mostrar média da turma")
    print("5 - Sair")


def main():
    """Laço principal do menu."""
    alunos = []

    while True:
        limpar_terminal()
        mostrar_menu()
        opcao = input("Escolha uma opção (1 a 5): ").strip()

        if opcao == "1":
            cadastrar_aluno(alunos)
        elif opcao == "2":
            listar_alunos(alunos)
        elif opcao == "3":
            buscar_aluno(alunos)
        elif opcao == "4":
            mostrar_media_turma(alunos)
        elif opcao == "5":
            print("Saindo do Sistema Escolar. Até mais!")
            break
        else:
            print("Opção inválida. Escolha um número de 1 a 5.")
            pausar()


if __name__ == "__main__":
    main()
