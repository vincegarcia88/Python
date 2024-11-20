class Conta:
    def __init__(self, titular, nib, saldo, pin):
        self.__titular = titular
        self.__nib = nib
        self.__saldo = saldo
        self.__limite = 400
        self.__pin = pin

    def __str__(self):
        return f'Titular: {self.titular}\nNIB: {self.nib}\nSaldo: {self.saldo}\nLimite: {self.limite:.2f}€'
        
    @property
    def titular(self):
        return self.__titular
        
    @property
    def nib(self):
        return self.__nib
        
    @property
    def saldo(self):
        return f'{self.__saldo:.2f}€'
        
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        
    @property
    def pin(self):
        return self.__pin
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f'{valor:.2f}€ depositados com sucesso.')
        else:
            print(f'Não é possivel depositar {valor:.2f}€ na sua conta.\nVisite o balcão mais próximo.')


    def levantar(self, valor):
        if valor <= self.__saldo and valor <= self.limite and valor > 0:
            self.__saldo -= valor
            print(f'{valor:.2f}€ levantados com sucesso.')
        else:
            print(f'Não é possivel levantar {valor:.2f}€ na sua conta.\nVisite o balcão mais próximo.')


    def transferir(self, conta, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            conta.depositar(valor)

    def obter_comprovativo_nib(self):
        from fpdf import FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt='COMPROVATIVO NIB', ln=1, align="C")
        pdf.cell(200, 10, txt=f'Titular: {self.titular}', ln=1, align="L")
        pdf.cell(200, 10, txt=f'NIB: {self.nib}', ln=1, align="L")
        pdf.output("comprovativo_nib.pdf")
        print('Comprovativo gerado com sucesso.')
