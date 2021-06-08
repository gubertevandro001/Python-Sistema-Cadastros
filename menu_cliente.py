
from Interfaces.cadastro_cliente import cadastro_cliente
from mostrar_cliente import mostrar_cliente


class MenuCliente():

    def menu_cliente(self):
        print(f'{"=" * 15}Menu do Cliente{"=" * 15}')
        escolha = input('1 - Cadastrar Cliente\n2 - Procurar Cliente\n3 - Mostrar Clientes\n4 - Sair\nInforme: ')

        if escolha == '1':
            cadastro_cliente.cadastrar_cliente()
            cadastro_cliente.continuar_cadastrando()
        elif escolha == '2':
            mostrar_cliente.mostrar_cliente_especifico()
            menu_clientes.entrar_menu_cliente()
        elif escolha == '3':
            mostrar_cliente.mostrar_clientes()
            menu_clientes.entrar_menu_cliente()
        else:
            print(f'{"=" * 20}Sistema de Cadastro(Clientes, Funcionários, Produtos){"=" * 20}')


    def entrar_menu_cliente(self):
        menu_clientes.menu_cliente()


menu_clientes = MenuCliente()
