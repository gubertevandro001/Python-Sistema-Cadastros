from Models.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome=None, idade=None, cpf=None, telefone=None, endereco=None, renda=None, limite_credito=0):
        super().__init__(nome, idade, cpf, telefone, endereco)
        self.renda = renda
        self.limite_credito = limite_credito

    def limite_credito_cliente(self):
        if cliente.renda < 1500:
            cliente.limite_credito = cliente.renda * 60 / 100
        else:
            cliente.limite_credito = cliente.renda * 80 / 100

        return cliente.limite_credito


cliente = Cliente()


