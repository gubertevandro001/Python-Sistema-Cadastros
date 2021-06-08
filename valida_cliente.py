from Models.cliente import cliente


class ValidaCliente():

    def valida_nome(self):
        cliente.nome = input('Nome: ')
        while cliente.nome.isnumeric() or len(cliente.nome) < 4:
            print('Nome Inválido!')
            return cliente_valida.valida_nome()
        else:
            pass

    def valida_idade(self):
        while True:
            try:
                cliente.idade = int(input('Idade: '))
            except ValueError:
                print('Idade Inválida!')
            else:
                break

    def valida_cpf(self):
        cliente.cpf = input('CPF: ')
        with open('clientes.csv', 'r+') as csvfile:
            while cliente.cpf in csvfile.read() or not cliente.cpf.isnumeric() or len(cliente.cpf) < 11:
                print('CPF Inválido!')
                return cliente_valida.valida_cpf()
            else:
                pass

    def valida_telefone(self):
        cliente.telefone = input('Telefone: ')
        while not cliente.telefone.isnumeric() or len(cliente.telefone) < 11:
            print('Telefone Inválido! Lembre-se do DDD')
            return cliente_valida.valida_telefone()
        else:
            pass

    def valida_endereco(self):
        cliente.endereco = input('Endereco: ')

    def valida_renda(self):
        while True:
            try:
                cliente.renda = float(input('Renda: '))
            except ValueError:
                print('Renda Inválida! ')
            else:
                break

cliente_valida = ValidaCliente()