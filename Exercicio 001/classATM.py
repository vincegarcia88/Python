#Class
class ATM:
    def __init__(self, contas):
        self.contas = contas

    def menu_inicial(self):
        while True:
            limpa()
            cabecalho('CAIXA MULTIBANCO')
            print('1 - Inserir Cartão')
            print('2 - Sair')
            opcao = int(input('--> '))

            if opcao == 1:
                self.menu_login(self.encontra_conta(pin=1))                      
            elif opcao == 2:
                aguarde()
                limpa()
                exit()
            else:
                print('Opção inválida.')

    def menu_login(self, conta):
        while True:
            limpa()
            cabecalho(f'BEM-VINDO(A) {conta.titular}')
            print('1 - Depositar')
            print('2 - Levantar')
            print('3 - Transferir')
            print('4 - Obter Comprovativo de NIB')
            print('5 - Verificar Saldo')
            print('6 - visualizar os dados da conta')
            print('7 - Retirar cartão')
            opcao = int(input('--> '))

            match opcao:
                case 1:
                    limpa()
                    aguarde()
                    limpa()
                    cabecalho('Depositar')
                    valor = float(input('Montante: '))
                    conta.depositar(valor)
                    clica_para_continuar()
                case 2:
                    limpa()
                    aguarde()
                    limpa()
                    cabecalho('Levantar')
                    valor = float(input('Montante: '))
                    conta.levantar(valor)
                    clica_para_continuar()
                case 3:
                    limpa()
                    aguarde()
                    limpa()
                    cabecalho('Transferir')
                    valor = float(input('Montante: '))
                    conta.transferir(self.encontra_conta(nib=1), valor)
                    clica_para_continuar()
                case 4:
                    limpa()
                    aguarde()
                    limpa()
                    conta.obter_comprovativo_nib()
                    clica_para_continuar()
                case 5:
                    limpa()
                    aguarde()
                    limpa()
                    print(conta.saldo)
                    clica_para_continuar()
                case 6:
                    limpa()
                    aguarde()
                    limpa()
                    print(conta)
                    clica_para_continuar()
                case 7:
                    limpa()
                    aguarde()
                    limpa()
                    break
                            
    def encontra_conta(self, nib=0, pin=0):
        if pin == 1 and nib == 0:
            pin = stdiomask.getpass('Digite o PIN: ', '*')
            for conta in self.contas:
                if conta.pin == pin:
                    aguarde()
                    return conta                   
            print('Não foi encontrada a sua conta.\nVisite o balcão mais próximo.')
        else:
            nib = input('Digite o NIB do beneficiário: ')
            for conta in self.contas:
                if conta.nib == nib:
                    aguarde()
                    print(f'Beneficiário: {conta.titular}')
                    clica_para_continuar()
                    aguarde()
                    return conta                   
            print('NIB inválido.\nVisite o balcão mais próximo.')
        aguarde()
        limpa()
        exit()