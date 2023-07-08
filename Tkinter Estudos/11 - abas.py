import tkinter as tk
from tkinter import ttk

#mainframe
window = tk.Tk()
window.title('Abas')
window.geometry('600x400')

#notebook widget
notebook = ttk.Notebook(window)

#aba 1
tab1 = ttk.Frame(notebook)

label1 = ttk.Label(tab1, text = 'Texto na aba 1')
label1.pack()

button1 = ttk.Button(tab1, text = 'Botão na aba 1')
button1.pack()

#aba 2
tab2 = ttk.Frame(notebook)

label2 = ttk.Label(tab2, text = 'Texto na aba 2')
label2.pack()

entry2 = ttk.Entry(tab2)
entry2.pack()

notebook.add(tab1, text = 'Aba 1')
notebook.add(tab2, text = 'Aba 2')

notebook.pack()


#exercicio
#adicionar mais uma aba com dois botoes e uma label dentro

#aba 3
aba3 = ttk.Label(notebook)
botao_ex = ttk.Button(aba3, text = 'botao1 ex')
botao_ex.pack()
botao_ex2 = ttk.Button(aba3, text = 'botao2 ex')
botao_ex2.pack()
labelex = ttk.Label(aba3, text = 'Texto do exercicio')
labelex.pack()


notebook.add(aba3, text = 'Aba 3 (Exercicio)')







#run
window.mainloop()