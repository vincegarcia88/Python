'''Crie um programa onde o utilizador possa inserir uma equação matemática
que use parênteses. O programa deverá analisar a equação e dizer se a equação
tem os parênteses corretos ou se está errado.

((a+b)-c(c/d) ((a+b)-c(c/d))'''

equacao = input('Digite a equação: ')

totParentesesEsquerda = equacao.count('(')
totParentesesDireita = equacao.count(')')

if totParentesesEsquerda == totParentesesDireita:
    print('A equação está correta')
else:
    print('A equação está incorreta.')