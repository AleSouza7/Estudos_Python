"""idade: int
salario: float; altura: float 
genero: str 
nome: str 
idade = 20 
salario = 5800.5 
altura = 1.63 
genero = "F" 
nome = "Maria Silva" 
print(f"IDADE = {idade}") 
print(f"SALARIO = {salario:.2f}") 
print(f"ALTURA = {altura:.2f}") 
print(f"GENERO = {genero}") 
print(f"NOME = {nome}") 
"""

"""print('boa noite' , end=' ')
print('boa noite')

x: int; y: int 
x = 10 
y = 20 
print(x) 
print(y) 

x: float 
x = 2.3456 
print("{:.2f}".format(x))"""

"""idade: int 
salario: float 
nome: str 
sexo: str 
"""
"""idade = 32 
salario = 4560.9 
nome = "Maria Silva" 
sexo = "F" 

print(f'A funcionária {nome}, do sexo {sexo}, tem um salário de R$ {salario:.2f} e tem {idade} anos de idade.')
print("A funcionaria {:s}, do sexo {:s}, tem um salário de R$ {:.2f} e tem {:d} anos de idade.".format(nome,sexo,salario,idade))
"""
"""
print(f"A funcionaria {nome}, sexo {sexo}, ganha {salario:.2f} e tem {idade} anos") 
print("A funcionaria {:s}, sexo {:s}, ganha {:.2f} e tem {:d} anos".format(nome, sexo, salario, idade))"""

salario1: float; salario2: float 
nome1: str; nome2: str 
idade: int 
sexo: str 

nome1 = input("Nome da primeira pessoa: ") 
salario1 = float(input("Salario da primeira pessoa: ")) 
nome2 = input("Nome da segunda pessoa: ") 
salario2 = float(input("Salario da segunda pessoa: ")) 
idade = int(input("Digite uma idade: ")) 
sexo = input("Digite um sexo (F/M): ") 

print(f"Nome 1: {nome1}") 
print(f"Salario 1: {salario1:.2f}") 
print(f"Nome 2: {nome2}") 
print(f"Salario 2: {salario2:.2f}") 
print(f"Idade: {idade}") 
print(f"Sexo: {sexo}") 