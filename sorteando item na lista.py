import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Sgundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1,n2,n3,n4]
sorteio = random.choice(lista)
print(f'O aluno escolhindo foi: {sorteio}')
