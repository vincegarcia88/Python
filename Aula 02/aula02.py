nome = "Alfredo Paiva"

#
print (nome[5])

print (nome [0:6])

#0 até o 7, de 2 em 2
print (nome[0:7:2])

#0 até o final
print (nome [0:])

#8 até o final
print (nome [8:])

#Largura do nome
print (len (nome))


print (nome.count ("a"))

print (nome.find ("z"))

#Replace
print (f"No início o nome era: {nome}")
nome.replace ("Alfredo", "Jéssica")

print (f"Agora é {nome}")

nome = input ("Digite seu nome: ")
print (nome)
print (len (nome))

nome = nome.strip ()
print (nome)
print (len (nome))

nome = " ".join (nome)
print (nome)
print (len (nome))

nome = nome.split ()
print (nome [1][0])

