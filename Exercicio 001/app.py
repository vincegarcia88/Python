"""Idealize um ATM (Caixa Multibanco) onde seja possível
introduzir um cartão e inserir o código. Aquando da introdução
correta do código abra um menu onde se poderá depositar,
levantar, transferir, obter comprovativo de NIB (gera um PDF),
verificar saldo e visualizar os dados da conta. Coloque todas
essas funcionalidades em ação."""

from class_atm import ATM
from constantes import CONTAS

def main():
    atm = ATM(CONTAS)
    atm.menu_inicial()

if __name__ == '__main__':
    main()

    from utils import *
import stdiomask