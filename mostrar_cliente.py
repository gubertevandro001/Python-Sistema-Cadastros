import csv

from Interfaces.cadastro_cliente import lista

class MostrarCliente():

    def mostrar_cliente_especifico(self):
        mostrar = input('\nInforme o CPF do Cliente: ')
        while not mostrar.isnumeric() or len(mostrar) != 11:
            print('CPF Inválido!')
            return mostrar_cliente.mostrar_cliente_especifico()
        else:
            with open('clientes.csv', 'r', newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')

                for linha in spamreader:
                    lista.append(linha)

                for k, v in enumerate(lista):
                    if mostrar in lista[k]:
                        print(f'\nNome: {lista[k][0]}\nIdade: {lista[k][1]}\nCPF: {lista[k][2]}\nTelefone: {lista[k][3]}\n'
                              f'Renda: {lista[k][4]}\nLimite Crédito: {lista[k][5]}\n')
                        lista.clear()


    def mostrar_clientes(self):
        with open('clientes.csv', 'r', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter= ',' )

            for linha in spamreader:
                lista.append(linha)

            for k, v in enumerate(lista):
                print(f'\nNome: {lista[k][0]}\nIdade: {lista[k][1]}\nCPF: {lista[k][2]}\nTelefone: {lista[k][3]}\n'
                      f'Renda: {lista[k][4]}\nLimite Crédito: {lista[k][5]}\n', end='')
            print()
            lista.clear()


mostrar_cliente = MostrarCliente()

