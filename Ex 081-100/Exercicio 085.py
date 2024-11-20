"""Crie um código em Python que teste se o
site do IEFP está acessível a partir do
seu computador."""

import urllib.request

try:
    ligacao = urllib.request.urlopen('https://www.iefp.pt/en')

except:
    print('O site não está disponível...')

else:
    print('O site está disponível.')