import csv

from Models.funcionario import funcionario
import Telas.menu_funcionario
from mensagens import mensagem
from valida_funcionario import funcionario_valida


class CadastroFuncionario():

    def cadastrar_funcionario(self):
        mensagem.mensagem_cadastrar_funcionario()
        funcionario_valida.valida_nome()
        funcionario_valida.valida_idade()
        funcionario_valida.valida_cpf()
        funcionario_valida.valida_telefone()
        funcionario_valida.valida_salario()
        cadastro_funcionario.salva_funcionarios()


    def continuar_cadastrando(self):
        escolha = input('Deseja Continuar Cadastrando Funcionários?\nS - Sim\nN - Não\nInforme: ')

        if escolha == '1':
            cadastro_funcionario.cadastrar_funcionario()
            return cadastro_funcionario.continuar_cadastrando()
        else:
            Telas.menu_funcionario.menu_funcionario.entrar_menu_funcionario()

    def salva_funcionarios(self):
        with open('funcionarios.csv', 'a', newline='') as csvfile:
            spamwrite = csv.writer(csvfile, delimiter=',')
            spamwrite.writerow([funcionario.nome, funcionario.idade, funcionario.cpf, funcionario.telefone, funcionario.salario, funcionario.vale_transporte_funcionario()])
            csvfile.close()


cadastro_funcionario = CadastroFuncionario()