#Array Multidimensional

turma = list ()
aluno = list()

for c in range (0,3):
    aluno.append (input("Digite o nome do aluno: "))
    aluno.append (input("Digite o ID do aluno: "))
    aluno.append (input("Digite a média do aluno: "))

    turma.append(aluno [:])
    aluno.clear ()

print ("Ler dados da turma: \n")

for linha in range (0,3):
    print ()
    for coluna in range (0,3):
        print(f"{turma [linha][coluna]}", end="\t")
        print ()
