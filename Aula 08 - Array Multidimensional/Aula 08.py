'''Array Multidimensional'''

alunos = list()
notas = list()

for linha in range (0,3):
    for coluna in range (0,5):
        nota = float(input(f"Digite uma nota para o {linha + 1}º aluno: "))
        notas.insert (coluna, nota)
    alunos.append(notas[:])

print (alunos)