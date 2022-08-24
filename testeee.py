from tkinter import *
from tkinter import ttk

app = Tk()
app.title('teste')
app.geometry('600x320')


tv = ttk.Treeview(app,columns=('Valor', 'Nome', 'Data','Recorrente'), show='headings')
tv.column('Valor', minwidth=0, width=100)
tv.column('Nome', minwidth=0, width=250)
tv.column('Data', minwidth=0, width=100)
tv.column('Recorrente', minwidth=0, width=100)
tv.heading('Valor', text='Valor')
tv.heading('Nome', text='Nome')
tv.heading('Data', text='Data')
tv.heading('Recorrente', text='Recorrente')
tv.pack()

app.mainloop()
