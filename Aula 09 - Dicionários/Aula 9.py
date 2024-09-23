#Exemplo em lista

aluno = list ()

aluno.append (input("Digite o nome: "))
aluno.append (input("Digite a idade: "))

print (aluno)

#Dicionário abaixo__________________________________

aluno = dict()

aluno ["Nome"] = "Ricardo"
aluno ["Idade"] = 32

print (aluno.items)
print (aluno.values)
print (aluno.keys)

#______________________________________________

for k, v in aluno.items():
    print (f"O {k} é {v}")

#______________________________________________

for c in range (0,3):
    aluno ["Nome"] = input (f"Digite o nome do {c+1}º aluno: ")
    aluno ["Idade"] = input (f"Digite a idade do {c+1}º aluno: ")

    turma.append (aluno.copy())

print (turma [0])