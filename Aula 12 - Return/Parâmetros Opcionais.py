def soma(a=0, b=0, c=0, mostra=False):
    soma_num = a + b + c
    if mostra:
        print(f'{a} + {b} + {c} = {soma_num}')
    else:
        print(soma_num)


soma(2, 3, 5)
soma(3, 5)
soma()