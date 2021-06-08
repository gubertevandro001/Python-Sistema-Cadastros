import csv

lista_f = []

class MostrarFuncionario():

    def mostrar_funcionario_especifico(self):
        mostrar = input('\nInforme o CPF do Funcionário: ')
        while not mostrar.isnumeric() or len(mostrar) != 11:
            print('CPF Inválido!')
            return mostrar_funcionario.mostrar_funcionario_especifico()
        else:
            with open('funcionarios.csv', 'r', newline='') as csvfile:
                spamread = csv.reader(csvfile, delimiter=',')

                for linha in spamread:
                    lista_f.append(linha)

                for k, v in enumerate(lista_f):
                    if mostrar in lista_f[k]:
                         print(f'\nNome: {lista_f[k][0]}\nIdade: {lista_f[k][1]}\nCPF: {lista_f[k][2]}\nTelefone: {lista_f[k][3]}\
                              \nSalário R$: {lista_f[k][4]}\nVale Transporte R$: {lista_f[k][4]}')
                         print()
                         lista_f.clear()


    def mostrar_funcionarios(self):
        with open('funcionarios.csv', 'r', newline='') as csvfile:
            spamread = csv.reader(csvfile, delimiter=',')

            for linha in spamread:
                lista_f.append(linha)

            for k, v in enumerate(lista_f):
                print(f'\nNome: {lista_f[k][0]}\nIdade: {lista_f[k][1]}\nCPF: {lista_f[k][2]}\nTelefone: {lista_f[k][3]}\
                      \nSalário R$: {lista_f[k][4]}\nVale Transporte R$: {lista_f[k][5]}')
            print()
            lista_f.clear()



mostrar_funcionario = MostrarFuncionario()
