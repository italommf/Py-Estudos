'''
pack:   nos deixa colocar de baixo para cima, 
        da esquerda para direita e da direita para a esquerda

grid:   nos deixa colocar em posições esspecíficas (imagina um grid mesmo)

place: coloca em qualquer lugar

'''
import tkinter as tk
from tkinter import ttk

#mainframe
window = tk.Tk()
window.title('caixas de seleção de menu e de rolagem')
window.geometry('600x400')


#widgets
label1 = ttk.Label(window, text = 'label1', background = 'red')
label2 = ttk.Label(window, text = 'label2', background = 'blue')

#pack
#label1.pack(side = 'left', expand = True, fill = 'both') # expand usa todo o espaço disponível para o widget
#label2.pack(side = 'right', expand = True, fill = 'x') # fill usa 'x', 'y' ou 'both' para preencher

#grid          numero da coluna, "peso" da coluna.
'''
window.columnconfigure(0, weight = 1) # Coluna 0, 1 coluna de tamanho
window.columnconfigure(1, weight = 1) # Coluna 1, 1 coluna de tamanho
window.columnconfigure(2, weight = 2) # Coluna 2, 2 colunas de tamanho
window.rowconfigure(0, weight = 1)
window.rowconfigure(1, weight = 1)
window.rowconfigure(2, weight = 1)

label1.grid(row = 0, column = 1, sticky = 'nsew')
label2.grid(row = 1, column = 1, columnspan = 2, sticky = 'nsew')
'''

#place
label1.place(x = 100, y = 200, width = 70, height = 25) # x e y começam em 0 a partir de cima na esquerda
label2.place(relx = 0.5, rely =  0.5, relwidth = 1, anchor = 'se') 

#run
window.mainloop()
