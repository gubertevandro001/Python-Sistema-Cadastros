from Models.funcionario import funcionario


class ValidaFuncionario():


    def valida_nome(self):
        funcionario.nome = input('Nome: ')
        while funcionario.nome.isnumeric() or len(funcionario.nome) < 4:
            print('Nome Inválido!')
            return funcionario_valida.valida_nome()
        else:
            pass

    def valida_idade(self):
        while True:
            try:
                funcionario.idade = int(input('Idade: '))
            except ValueError:
                print('Idade Inválida!')
            else:
                break

    def valida_cpf(self):
        funcionario.cpf = input('CPF: ')
        with open('funcionarios.csv', 'r+') as csvfile:
            while funcionario.cpf in csvfile.read() or not funcionario.cpf.isnumeric() or len(funcionario.cpf) != 11:
                print('CPF Inválido!')
                return funcionario_valida.valida_cpf()
            else:
                pass

    def valida_telefone(self):
        funcionario.telefone = input('Telefone: ')
        while not funcionario.telefone.isnumeric() or len(funcionario.telefone) < 11:
            print('Telefone Inválido! Lembre-se do DDD')
            return funcionario_valida.valida_telefone()
        else:
            pass

    def valida_salario(self):
        funcionario.salario = input('Salário R$: ')
        while not funcionario.salario.isnumeric():
            print('Salário Inválido!')
            return funcionario_valida.valida_salario()
        else:
            pass


funcionario_valida = ValidaFuncionario()