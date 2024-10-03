"""Crie um programa que tenha uma função que receba um texto como parâmetro e que
mostre uma mensagem com tamanho adaptável.

Ex:
mostre(“Olá mundo.”)
Saída:
-=-=-=-=-=-=-=-=
Olá mundo.
-=-=-=-=-=-=-=-="""

def mostra_texto (txt):
    tam = int(len (txt/2)) + 2
    print("-=\n" * tam)
    print (f"{txt:^ {tam*2}}")
    print("-=" * tam)

    mostra_texto("Python")
