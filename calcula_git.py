# @author cassiano watte | cassianowatte@gmail.com
# @description this is a study case

# used because
from optparse import Option
from turtle import down
from typing import Any
from webbrowser import get
import pandas as pd
import os
import csv
from tkinter import *
from tkinter.ttk import *

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


def insert_compensation(valor,nome,data,recorrente,nova_janela):
    valor_entradas = valor
    nome_entradas = nome
    data_entradas = data
    recorrente_entradas = recorrente
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
    ok = Label(nova_janela, text='Informações Inseridas com Sucesso!', font='Arial')
    ok.pack(side=BOTTOM)
    


def insert_spent(valor,nome,data,recorrente):
    valor_saida = valor
    nome_saida = nome
    data_saida = data
    recorrente_saida = recorrente
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


def insert_payment(valor,nome,data,pago):
    valor_pagamento = valor
    descricao_pagamento = nome
    data_pagamento = data
    input_pago = pago
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

janela = Tk()
janela.title('Calcula Python')
janela.geometry('512x256')





def nova_janela(a):
    nova_janela = Toplevel(janela)
    nova_janela.title('Calcula Python')
    nova_janela.geometry('512x256')
    Label(nova_janela, text='Insira as informações!').pack()
    
    valor = Label(nova_janela, text='Valor:', font='arial',)
    valor.place(relx=0.1, rely=0.30, relwidth=0.15, relheight=0.1)
    nome = Label(nova_janela, text='Nome:', font='arial')
    nome.place(relx=0.1, rely=0.42, relwidth=0.15, relheight=0.1)
    data = Label(nova_janela, text='Data:', font='arial')
    data.place(relx=0.1, rely=0.54, relwidth=0.15, relheight=0.1)
    recorrente = Label(nova_janela, text='Recorrente:', font='arial')
    recorrente.place(relx=0.1, rely=0.66, relwidth=0.17, relheight=0.1)
    entry1 = Entry(nova_janela, font=('arial', 11, 'bold'))
    entry1.place(relx=0.2, rely=0.30, relwidth=0.20, relheight=0.1)
    entry2 = Entry(nova_janela, font=('arial', 11, 'bold'))
    entry2.place(relx=0.2, rely=0.42, relwidth=0.35, relheight=0.1)
    entry3 = Entry(nova_janela, font=('arial', 11, 'bold'))
    entry3.place(relx=0.2, rely=0.54, relwidth=0.20, relheight=0.1)
    entry4 = Entry(nova_janela, font=('arial', 11, 'bold'))
    entry4.place(relx=0.27, rely=0.66, relwidth=0.15, relheight=0.1)
    if a == 1:
        botaoadd = Button(nova_janela, text='SALVAR',command=lambda: insert_compensation(entry1.get(), entry2.get(), entry3.get(), entry4.get(), nova_janela))
        botaoadd.pack()
        
        
            

        
    if a == 2:
        botaoadd = Button(nova_janela, text='SALVAR',command=lambda: insert_spent(entry1.get(), entry2.get(), entry3.get(), entry4.get()))
        botaoadd.pack()

    if a == 3:
        botaoadd = Button(nova_janela, text='SALVAR',command=lambda: insert_payment(entry1.get(), entry2.get(), entry3.get(), entry4.get()))
        botaoadd.pack()




    





texto_orientacao = Label(janela, text='Escolha a Opção desejada!')
texto_orientacao.grid(column=0, row=0)

botao1 = Button(janela, text='Inserir Entradas', command=lambda: nova_janela(1))
botao1.grid(column=5, row= 5)

botao2 = Button(janela, text='Inserir Saidas', command=lambda: nova_janela(2))
botao2.grid(column=5, row=6)

botao3 = Button(janela, text='Inserir Pagamentos', command=lambda: nova_janela(3))
botao3.grid(column=5, row=7)





janela.mainloop()



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
