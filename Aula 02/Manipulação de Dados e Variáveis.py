#Precisão de ponto flutuante: {:.2f}. Isto irá formatar um
#número flutuante para ter duas casas decimais.
#Largura e alinhamento: {:<10}. Isto irá alinhar o valor à
#esquerda dentro de um espaço de 10 caracteres.

#2 casas decimais
numero = 123.456789
print(f"{numero:.2f}")

#3 casas decimais
numero = 56.6679988
print (f"{numero:.3f}")

# Alinhar à esquerda
numero = 1974
print (f"{numero:<10}")

# Alinhar À direita
numero = 1988
print (f"{numero:>10}")

# Largura e alinhamento ao centro
numero = 1986
print(f"{numero:^10}")

# Preenchimento de caracteres
numero = 1962
print (f"{numero:x<10}")

# Formatação de porcentagem (Transforma float em porcentagem)
numero = 90.0
print (f"{numero:.1%}")

# Separador de milhares
numero = 70000000
print (f"{numero:,}")