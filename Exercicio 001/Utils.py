def cabecalho(txt):
    print(f'--- {txt} ---\n')

def limpa():
    import os
    os.system('cls')

def aguarde():
    from time import sleep
    texto = 'Por favor aguarde...'
    for letra in texto:
        print(letra, end='', flush=True)
        sleep(0.1)
    print()

def clica_para_continuar():
    _ = input('Enter para continuar...')
