class Conta():

    def __init__(self, saldo):

        self.saldo = saldo

    def depositar(self, quant):
        if quant > 0:
            self.saldo += quant

            print(f'\n------------------ voce depositou {quant} R$ e agora o seu saldo é de {self.saldo} R$ ------------------')

            return self.saldo
        else:
            print('\n------------------* Digite um numero valido * ------------------')

    def sacar(self, quant):
        if quant <= 0:
            print('\n------------------* Digite um numero valido * ------------------')

        elif self.saldo - quant < 0:
            print(f'\n------------------ voce tentou sacar {quant} R$ mas voce não tem saldo suficiente para fazer este saque, seu saldo é de {self.saldo} R$ ------------------')

        else:
            self.saldo -= quant

            print(f'\n------------------ voce sacou {quant} R$ e agora o seu saldo é de {self.saldo} R$ ------------------')

            return self.saldo

















