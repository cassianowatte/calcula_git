# @author cassiano watte | cassianowatte@gmail.com
# @description this is a study case

# used because
import pandas as pd
import os
import csv

coloumns_names = [
    'Valor', 'Nome', 'Data', 'Recorrente'
]
coloumns_names2 = [
    'Valor', 'Nome', 'Data', 'Pago'
]


class ContentTable:

    def inputData(self, entrada=None, nome=None, data=None, recorrente=None, saida=None):
        if entrada is not None:
            self.user_input = entrada
        if nome is not None:
            self.user_name = nome
        if data is not None:
            self.user_date = data
        if recorrente is not None:
            self.user_continuous = recorrente
        if saida is not None:
            self.user_output = saida

    def string_format(self):
        if(hasattr(self, 'user_output') == False):
            return '{} , {} , {} , {}'.format(self.user_input, self.user_name, self.user_date, self.user_continuous)
        return '{} , {} , {} , {}'.format(self.user_output, self.user_name, self.user_date, self.user_continuous)

    def getListFormat(self):
        if(hasattr(self, 'user_output') == False):
            return [self.user_input, self.user_name, self.user_date, self.user_continuous]
        return [self.user_output, self.user_name, self.user_date, self.user_continuous]


def insert_compensation(option):
    valor_entradas = float(input('Valor da conta:'))
    data_entradas = str(input('Digite a data: '))
    nome_entradas = str(input('Nome da Entrada: '))
    recorrente_entradas = str(input('Recorrente [S/N]: ')).strip().upper()
    if recorrente_entradas in 'Ss':
        recorrente_entradas = 'sim'
    else:
        recorrente_entradas = 'nao'
    tabela = ContentTable()
    tabela.inputData(valor_entradas, nome_entradas,
                     data_entradas, recorrente_entradas)
    # if data.csv doesn't exist create it
    diretorio = ('compensation.csv')
    if os.path.isfile(diretorio) == False:
        with open('compensation.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow((coloumns_names))
            csvfile.write('\n')
            csvfile.close()
    csvFormat = pd.read_csv('compensation.csv', sep=',')
    csvFormat = pd.concat([csvFormat, pd.DataFrame(
        [tabela.getListFormat()], columns=coloumns_names)])
    csvFormat.to_csv('compensation.csv', index=False)
    print('valores de entradas inseridos com sucesso!')


def insert_spent(option):
    valor_saida = float(input('Valor da saida: '))
    data_saida = str(input('Data da saida: '))
    nome_saida = str(input('Descrição da saida: '))
    recorrente_saida = str(input('recorrente [S/N]: ')).strip().upper()
    if recorrente_saida in 'sS':
        recorrente_saida = 'sim'
    else:
        recorrente_saida = 'nao'
    tabela = ContentTable()
    tabela.inputData(valor_saida, nome_saida, data_saida, recorrente_saida)
    diretorio = ('spent.csv')
    if os.path.isfile(diretorio) == False:
        with open('spent.csv', 'w') as f:
            f.write(','.join(coloumns_names))
            f.write('\n')
            f.close()
    csvFormat = pd.read_csv('spent.csv', sep=',')
    csvFormat = pd.concat([csvFormat, pd.DataFrame(
        [tabela.getListFormat()], columns=coloumns_names)])
    csvFormat.to_csv('spent.csv', index=False)
    print('valores de saídas inseridos com sucesso!'
          )


def insert_payment(option):
    valor_pagamento = float(input('Valor do pagamento: '))
    data_pagamento = str(input('Data do pagamento: '))
    descricao_pagamento = str(input('Descrição do pagamento: '))
    input_pago = str(input('Pago [S/N]: ')).strip().upper()
    if input_pago in 'Ss':
        input_pago = 'sim'
    else:
        input_pago = 'nao'
    tabela = ContentTable()
    tabela.inputData(valor_pagamento, descricao_pagamento,
                     data_pagamento, input_pago)
    diretorio = ('payment.csv')
    if os.path.isfile(diretorio) == False:
        with open('payment.csv', 'w') as f:
            f.write(','.join(coloumns_names2))
            f.write('\n')
            f.close()
    csvFormat = pd.read_csv('payment.csv', sep=',')
    csvFormat = pd.concat([csvFormat, pd.DataFrame(
        [tabela.getListFormat()], columns=coloumns_names2)])
    csvFormat.to_csv('payment.csv', index=False)
    print('valores de pagamento inseridos com sucesso!')


def query_compensation(option):
    consulta_entradas1 = str(input('Entrada desejada: '))
    with open('compensation.csv', 'r') as f:
        exibir = f.readlines()
    print('Valor | Nome | Data | Recorrente')
    for linha in exibir:
        if consulta_entradas1 in linha:
            print(linha)


def query_spent(option):
    consulta_saidas1 = str(input('Saída desejada: '))
    with open('spent.csv', 'r') as f:
        exibir = f.readlines()
    print('Valor | Nome | Data | Recorrente')
    for linha in exibir:
        if consulta_saidas1 in linha:
            print(linha)


def query_payment(option):
    consulta_payment = str(input('Pagamento desejado: '))
    with open('payment.csv', 'r') as f:
        exibir = f.readlines()
    print('Valor | Nome | Data | Pago')
    for linha in exibir:
        if consulta_payment in linha:
            print(linha)


def main():
    # TODO verify if the file data and spent files already exists
    # if not create both with columns names
    # input (user_input, self.user_name, self.user_date, self.user_continuous)
    # output (self.user_output, self.user_name, self.user_date, self.user_continuous)
    while True:

        print('''Digite a opção desejada:
        [1] inserir entradas
        [2] inserir saidas
        [3] inserir pagamento
        [4] consultar entradas
        [5] consultar saidas
        [6] consultar pagamentos
        
        ''')
        options = {
            1: insert_compensation,
            2: insert_spent,
            3: insert_payment,
            4: query_compensation,
            5: query_spent,
            6: query_payment

        }

        option = int(input('Which option would you like to perform? '))
        options.get(option)(option)


if __name__ == "__main__":
    main()
