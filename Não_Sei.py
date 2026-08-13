#Exercício de criação de sistema

#===== Sistema Escolar =====
#1 - Cadastrar aluno
#2 - Listar alunos
#3 - Buscar aluno
#4 - Mostrar média da turma
#5 - Sair

import os #importando um tipo de sistema pronto

alunos =  []

while True:
    #Limpando o terminal
    os.system('clear')

    print("======= Sistema Escolar =======")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("4 - Mostrar média da turma")
    print("5 - Sair")

    opção = input ("Escolha uma opção(número): ")

    if opção ==  "1":
            
        Nome = input ("Nome do aluno?")
        while True:
            try:
                Idade = int(input("Qual a idade do aluno? "))
                break
            except ValueError:
                print("Entrada inválida! Por favor, digite apenas números.")
        while True:        
            try:
                Nota1 = float(input("Nota 1: "))
                break
            except ValueError:
                print("Entrada inválida! Por favor, digite uma nota válida.")
        while True:        
            try:
                Nota2 = float(input("Nota 2: "))
                break
            except ValueError:
                print("Entrada inválida! Por favor, digite uma nota válida.")

        Média = (Nota1 + Nota2) /   2

        if Média >= 7:
            situação = "Aprovado"
        else:
            situação = "Reprovado"
        aluno_novo = {
            "Nome": Nome,
            "Idade": Idade,
            "Nota1": Nota1,
            "Nota2": Nota2,
            "Média": Média,
            "Situação": situação
        }
        alunos.append(aluno_novo)
        print("aluno novo cadastrado com sucesso!")
        input("Pressione ENTER para continuar...")
    
    elif opção == "2":
        if len(alunos) == 0:
            print ("Nenhum aluno cadastro")
        else:
            for aluno in alunos:
                print(f"Nome: {aluno['Nome']}")
                print(f"Idade: {aluno['Idade']}")
                print(f"Média: {aluno['Média']:.2f}")
                print(f"Situação: {aluno['Situação']}")
                print ("-----------------")
        input("Pressione ENTER para continuar...")

    elif opção == "3":

        if len(alunos) == 0:
            print("Nenhum aluno cadastrado")

        else:
            busca = input("Qual o nome do aluno? ")
            encontrado = False
            for aluno in alunos:

                if aluno["Nome"].lower() == busca.lower():

                    print("\n--- Aluno Encontrado ---")
                    print(f"Nome: {aluno['Nome']}")
                    print(f"Idade: {aluno['Idade']}")
                    print(f"Nota1: {aluno['Nota1']}")
                    print(f"Nota2: {aluno['Nota2']}")
                    print(f"Média: {aluno['Média']:.2f}")
                    print(f"Situação: {aluno['Situação']}")
                    encontrado = True
                    break

        if not encontrado:
            print("Aluno não encontrado")
        input("Pressione ENTER para continuar...")

    elif opção == "4":
        quantidade_alunos = len(alunos)
        if quantidade_alunos == 0:
            print("Não há alunos cadastrados")

        else:
            soma_geral = 0
            for aluno in alunos:
                soma_geral += aluno["Média"]

            media_geral = soma_geral / quantidade_alunos
            print(f"A média geral da turma é: {media_geral:.2f}")
        input("Pressione ENTER para continuar...")

    elif opção == "5":
        print ("Saindo do Sistema")
        break
    else:
        print("Opção invalida, escolha um numero de 1 a 5")
        input("Pressione ENTER para continuar...")
