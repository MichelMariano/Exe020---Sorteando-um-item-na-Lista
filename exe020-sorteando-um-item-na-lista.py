
#Exercício Python 20: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
n5 = str(input('Quinto Aluno: '))

lista = [n1, n2, n3, n4]    #Coloco dentro dos parenteses os alunos que vão participar do sorteio

escolhido = random.choice(lista)

print('O aluno escolhido foi {} '.format(escolhido))
