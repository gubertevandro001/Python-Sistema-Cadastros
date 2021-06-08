from time import sleep
from Telas.menu_cliente import menu_clientes
from Telas.menu_funcionario import menu_funcionario


class Sistema():

    def acesso_sistema(self):
        print(f'{"=" * 20}Sistema de Cadastro(Clientes, Funcionários, Produtos){"=" * 20}')
        while True:
            try:
                escolha = int(input('1 - Menu Clientes\n2 - Menu Funcionários\n3 - Sair do Sistema\nInforme: '))

                if escolha == 1:
                    menu_clientes.entrar_menu_cliente()
                elif escolha == 2:
                    menu_funcionario.entrar_menu_funcionario()
                else:
                    print('Encerrando o Sistema...!')
                    sleep(3)
                    print('Sistema Encerrado!')
                    exit()
            except ValueError:
                print('Opção Inválida!')

    def sistema(self):
        entrar_sistema.acesso_sistema()

entrar_sistema = Sistema()
