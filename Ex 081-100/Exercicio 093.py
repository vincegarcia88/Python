"""Crie uma classe ContaBancaria com atributos titular, saldo e limite.
Adicione métodos para depositar() e sacar(), alterando o saldo da conta de
acordo com a operação."""

import os

def cabecalho (msg):
    print(msg)

def limpa():
    os.system("cls")

class ContaBancaria:
    def __init__(self, titular, saldo, limite, pin):
        self.titular = titular
        self.saldo = saldo
        self.limite = 400
        self.pin = pin

    def depositar (self, valor):
        self.saldo += valor
    
    def sacar (self, valor):
        self.saldo -= valor
    
    ######## Programa Principal #######
    while True:

    limpa ()
    cabecalho()
    print("1 - Registrar conta")
    print("2 - Inserir cartão")
    print("3 - Sair")
    opcao = int(input("---->"))

    match (opcao):
        case 1: 
            limpa()
            cabecalho("---Registrar conta ---")
            titular = input("Titular: ")
            saldo = float(input("Saldo: "))
            pin = input("PIN: ")
            conta = ContaBancaria(titular, saldo)

        case 2: 
            limpa()
            cabecalho("--- Inserir Cartão ---")
            pin = input("Digite o seu PIN: ").strip()
            if pin == conta.pin:
                limpa()
                cabecalho(f"--- Bem vindo{conta.titular}---")
                print("1 - Depositar")
                print("2 - Sacar")
                print("3 - Sair")
                opcao = int(input("--->"))
            
            


