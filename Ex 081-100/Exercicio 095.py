"""Crie uma classe ContaBancaria com atributos privados nib, titular, saldo e
limite. Adicione métodos getters e setters para os atributos."""


class ContaBancaria:
    # método construtor
    def __init__(self, nib, titular, saldo):
        self.__nib = nib
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = 400
        self.__login = True

    def get_nib(self):
        return self.__nib

    def get_titular(self):
        return self.__titular

    def set_titular(self, novo_titular):
        self.__titular = novo_titular

    def get_saldo(self):
        if self.get_login():
            return self.__saldo
        else:
            return f'Estado login: {self.get_login()}'

    def get_limite(self):
        return self.__limite

    def get_login(self):
        return self.__login


nova_conta = ContaBancaria(1234, 'Euzinho', 500)

print(nova_conta.get_saldo())