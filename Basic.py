"""
==========================================
PYTHON FUNDAMENTALS - CHEAT SHEET

Topics Covered:

✓ Strings
✓ Variables
✓ Type Conversion
✓ Input / Output
✓ Operators
✓ Conditionals
✓ Loops
✓ Lists
✓ Tuples
✓ Sets
✓ Dictionaries
✓ Functions
✓ Built-in Functions
✓ Exceptions
✓ Modules

Author: Luís Fernando
==========================================
"""

# =====================================
#Strings
# =====================================

name = "Luffy"

print(name.upper())
print(name.lower())
print(name.replace("Luffy", "Zoro"))
print(len(name))

# =====================================
#métodos de string
# =====================================

text = "Python"

print(text.startswith("Py"))
print(text.endswith("on"))
print(text.find("th"))
print(text.split("t"))

# =====================================
#Slicing (serve para pegar uma parte de uma sequência: como uma string, lista ou até bytes.)
# =====================================
name = "Luffy"

print(name[0])
print(name[1:4])
print(name[:3])
print(name[2:])
print(name[::-1])

# =====================================
# Variável
# =====================================

name_list = ["Luffy", "Zoro", "Nami"]
number_list = [1, 2, 3]
empty_list = []

# =====================================
#imprimir valores
# =====================================

print (name)
print (age)
print (weight)

#======================================
#F-String (acesso rápido a uma String)
#======================================
name = "Luffy"
age = 19

print(f"{name} have {age} years.")

# =====================================
#Conversão de tipos
# =====================================

number = "10"

print(int(number))
print(float(number))
print(str(10))

# =====================================
#Mostrar Tipos
# =====================================

print(type(10))
print(type(3.14))
print(type("Python"))
print(type(True))

# =====================================
#Leitura de dados
# =====================================

name1 = input("To type your name: ")
age1 = int (input("To type your age: "))
weight1 = float (input("To type your weight: "))

# =====================================
#imprimir valores que recebeu
# =====================================

print (name1)
print  (age1)
print (weight1)

# =====================================
# isinstance (Serve para verificar se um objeto pertence a um determinado tipo. Ele retorna um valor booleano )
# =====================================

print(isinstance(10, int))
print(isinstance("Python", str))

# =====================================
# Operadores lógicos
# =====================================

print(True and False)
print(True or False)
print(not True)

# =====================================
# Pass
# =====================================
if True:
    pass

# =====================================
# Operadores aritméticos
# =====================================

sum_ = 1 + 1
subtraction = 1 - 1
multiplication = 2 * 1
division = 2 / 1
potency = 2 ** 3

# =====================================
# Operadores relacionais
# =====================================

print(10 > 5)
print(10 < 5)
print(10 >= 5)
print(10 <= 5)
print(10 == 5)
print(10 != 5)

# =====================================
#imprimindo valores
# =====================================

print ("sum", sum) 
print ("subtraction", subtraction) 
print ("multiplication", multiplication)
print ("division", division)
print ("potency", potency)

# =====================================
#Condicionais
# =====================================

salario = int(input("To type your salary: ")) #Entrada
if salario == 0: #Se, faça:
    print("trainee programmer") 
elif salario < 3000: #Senão, se faça:
    print("Junior programmer")

elif salario < 7000: #Senão, se faça:
    print("Programador Pleno")
else: #Senão, faça:
    print("Programador Senior")

# =====================================
#usando o For para contar do 0 ao 10
# =====================================

for i in range(1, 11):
    print(i)

# =====================================
#Usando o for para percorrer uma lista
# =====================================

fruits = ["Apple", "Banana", "Grapple"]

for fruit in fruits:
    print(fruit)

# =====================================
#break e continue do for
# =====================================

for i in range(10):
    if i == 5:
        break

    print(i)

for i in range(10):

    if i == 5:
        continue

    print(i)    

# =====================================
#Usando o While como contador até a condição deixar de ser verdadeira
# =====================================

accountant = 1

while accountant <= 5:
    print(accountant)
    accountant += 1

# =====================================
#enumerate()
# =====================================

    fruits = ["Apple", "Banana", "Grapple"]

for index, fruit in enumerate(fruits): #Vai enumerar enquanto imprime  
    print(index, fruit)

# =====================================
#Tuplas
# =====================================

colors = ("Blue", "Green", "Red")
print(colors[0])

# =====================================
#Sets
# =====================================

numbers = {1,2,3,3,2,1}
print(numbers)

# =====================================
#Listas
# =====================================

list_names = ["Luffy", "Zoro", "Nami"]
print (list_names[0])

list_numbers = [1, 2, 3]
list_numbers[0] = 10

# =====================================
#imprimindo tamanho, valor minimo e valor maximo
# =====================================

print ("total: ", len(list_numbers))
print ("minimum value: ", min(list_numbers))
print ("maximum value: ", max(list_numbers))

list_empty = []

# =====================================
#Adicionar na lista
# =====================================
list_empty.append("Sanji")
list_empty.append("Chopper")
list_empty.append("Robin")
print (list_empty)

# =====================================
#Inserir na lista
# =====================================

list_empty.insert(1, "Usopp")

# =====================================
#Buscar na lista
# =====================================

if "Luffy" in list_names:
    print("The Luffy in list!")
else:
    print ("Not in list")

# =====================================
#Remover da lista
# =====================================

list_empty.remove("Chopper")

# =====================================
#Remover da lista o ultimo elemento e retorna o elemento removido
# =====================================

last_element = list_empty.pop()

# =====================================
#Remover da lista o elemento de acordo com o índice
# =====================================

element_removed = list_empty.pop(0)

# =====================================
#ordena a lista
# =====================================

list_empty.sort()

# =====================================
#Verifica se pelo menos um elemento é verdadeiro.
# =====================================

list = [False, False, True]
print(any(list))

# =====================================
#reverte a lista
# =====================================

list_empty.reverse()

# =====================================
#retorna o índice do elemento
# =====================================

index = list_empty.index("Usopp")

# =====================================
# Mostra o identificador do objeto na memória.
# =====================================

name = "Python"
print(id(name))

# =====================================
#retorna o numero de ocorrências do elemento na lista
# =====================================

occurrence = list_empty.count("Usopp")

# =====================================
#retornar quantos itens tem na lista
# =====================================

size = len(list_empty)

# =====================================
#List Comprehension
# =====================================

square = [i**2 for i in range(10)]
print(square)

# =====================================
#Tratamento de Exceções
# =====================================

try:
    age = int(input("age: "))
except ValueError:
    print("To type only numbers.")

# =====================================
#Mostrar parâmetros nomeados
# =====================================

def register(name, age):
    print(name, age)

register(age=20, name="Luis")

# =====================================
#laços de repetição
# =====================================

for i in range(5):
    print(i)

accountant = 1
while accountant <= 5:
    print(accountant)
    accountant += 1

# =====================================
#Dicionários (armazenam dados em pares de chave e valor)
# =====================================

one_piece = {"name": "Luffy", "age": 19, "weight": 65.0}
print(one_piece["name"])

# =====================================
#Percorrer o dicionário
# =====================================

for key, value in one_piece.items():
    print(key, value)
    print(one_piece.keys()) 

# =====================================
#Funções (utilizam parâmetros para receber dados e retornar valores)
# =====================================

def my_function(value1, value2):
    #valor1 e valor2 são parâmetros da função
    return value1 + value2

answer = my_function(10, 20) #definindo parâmetros
print("answer", answer)

# =====================================
#Funções com parâmetros opcionais
# =====================================

def salutation(name="Visitant"):
    print("Hi", name)

salutation()
salutation("Luis")

# =====================================
# Funções Embutidas (são funções que já vêm pronta, não precisa importar nenhuma biblioteca para usá-las)
# =====================================

print(abs(-10))
print(round(3.14159, 2))
print(sum([1,2,3]))
print(max([5,8,2]))
print(min([5,8,2]))

# =====================================
#Importação de módulos
# =====================================

import math
print(math.sqrt(25))

import random
print(random.randint(1,10))