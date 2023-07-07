import tkinter as tk
from tkinter import ttk
from random import choice

#mainframe
window = tk.Tk()
window.title('caixas de seleção de menu e de rolagem')
window.geometry('600x400')

#data
primeiro_nome = ['italo', 'lidiane', 'joao', 'paulo','Alex', 'James', 'Susan ', 'Henry ','Lisa', 'Anna', 'Lisa']
sobrenome = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

idade = [24, 24, 21, 24]

table = ttk.Treeview(window, columns = ('Nome', 'Idade', 'Email'), show = 'headings')
table.heading('Nome', text = 'Primeiro Nome')
table.heading('Idade', text = 'Idade')
table.heading('Email', text = 'Email')
table.pack(fill = 'both', expand = True)

#inserindo valores na tabela
#table.insert(parent = '', index = 0, values = ('Italo', 24, 'italo@mail.com'))
for i in range(100):
    p_nome = choice(primeiro_nome)
    s_nome = choice(sobrenome)
    email = f'{p_nome[0]}.{s_nome}@mail.com'
    data = (p_nome, s_nome, email)
    table.insert(parent = '', index = 0, values = data) # index é a posição da lista, o índice. para o fim da lista " index = tk.END "

#events

def item_select(_):
    for i in table.selection():
        print(table.item(i)['values'])

def delete_items(_):
    for i in table.selection():
        table.delete(i)

table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_items)

#run
window.mainloop()