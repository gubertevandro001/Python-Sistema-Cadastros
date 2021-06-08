from Telas.cadastro_funcionario import cadastro_funcionario
from mostrar_funcionario import mostrar_funcionario


class MenuFuncionario():


    def menu_funcionario(self):
        print(f'{"=" * 15}Menu do Funcionário{"=" * 15}')
        escolha = input('1 - Cadastrar Funcionario\n2 - Procurar Funcionario\n3 - Mostrar Funcionarios\n4 - Sair\nInforme: ')

        if escolha == '1':
            cadastro_funcionario.cadastrar_funcionario()
            cadastro_funcionario.continuar_cadastrando()
        elif escolha == '2':
            mostrar_funcionario.mostrar_funcionario_especifico()
            menu_funcionario.entrar_menu_funcionario()
        elif escolha == '3':
            mostrar_funcionario.mostrar_funcionarios()
            menu_funcionario.entrar_menu_funcionario()
        else:
            print(f'{"=" * 20}Sistema de Cadastro(Clientes, Funcionários, Produtos){"=" * 20}')


    def entrar_menu_funcionario(self):
        menu_funcionario.menu_funcionario()



menu_funcionario = MenuFuncionario()

