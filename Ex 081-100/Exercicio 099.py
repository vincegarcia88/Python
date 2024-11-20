'''Modifique o exercício 95 para ter atributos
privados para titular, saldo e limite.
Implemente getters e setters usando property
para esses atributos. Adicione métodos para
depositar() e sacar(), que devem alterar o
saldo da conta. Garanta que as operações
respeitem o limite da conta e que o saldo não
se torne negativo.'''

class ContaBancaria:
    def __init__(self,titular,saldo = 0,limite = 0):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite 

    @property
    def titular(self):
        return self.__titular 
    
    @titular.setter
    def titular(self,titular):
        self.__titular = titular

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            print("Saldo não pode ser negativo.")

    @property
    def limite(self):
        return self.__limite 
    
    @limite.setter
    def limite(self, novo_limite):
        if novo_limite >= 0:
            self.__limite = novo_limite
        else:
            print("O limite não pode ser negativo.")
    
    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
            print(f'Depósito de {valor} euros realizado. Saldo atual: {self.__saldo}')
        else:
            print(f'O valor do depósito deve ser positivo.')
            
    def sacar(self, novo_valor):
        if novo_valor <= 0:
            print("O valor do levantamento deve ser positivo.")
        elif novo_valor > self.__saldo + self.__limite:
            print("Saldo insuficiente para levantamento.")
        else:
            self.__saldo -= novo_valor
            print(f"Saque de {novo_valor} euros realizado. Saldo atual: {self.__saldo}")
        

# Criando uma conta bancária com saldo inicial e limite
conta = ContaBancaria("João Silva", saldo=1000, limite=500)

# Obtendo os dados da conta
print(f'TITULAR:',conta.titular)   # Exibe o titular
print(f'SALDO:',conta.saldo)   # Exibe o saldo
print(f'LIMITE:',conta.limite)   # Exibe o limite

# Atualizando o saldo da conta
conta.depositar(10)       
conta.sacar(100)        


   
