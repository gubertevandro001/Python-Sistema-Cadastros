from Models.pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome=None, idade=None, cpf=None, telefone=None, endereco=None, salario=None, vale_transporte=None):
        super().__init__(nome, idade, cpf, telefone, endereco)
        self.salario = salario
        self.vale_transporte = vale_transporte

    def vale_transporte_funcionario(self):
        if funcionario.salario:
            funcionario.vale_transporte = 180

        return funcionario.vale_transporte


funcionario = Funcionario()










