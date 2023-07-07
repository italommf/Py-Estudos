import tkinter as tk
from tkinter import ttk

#mainframe
window = tk.Tk()
window.title('caixas de seleção de menu e de rolagem')
window.geometry('600x400')

#combobox (caixas de seleção de menu)
itens = ('sorvete', 'bolo', 'pizza')
comida_str = tk.StringVar(value = itens[0]) # value pode ser texto, ex.: " value = 'comida favorita' "
combo = ttk.Combobox(window, textvariable = comida_str)
combo['values'] = itens # as duas fazem a mesma coisa, aqui é mais simples
#combo.configure(values = itens)
combo.pack()

#events
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text = f'Valor selecionado: {comida_str.get()}'))
combo_label = ttk.Label(window, text = 'a label')
combo_label.pack()

#spinbox
spin_int = tk.IntVar()
spin = ttk.Spinbox(window, 
                   from_ = 3, 
                   to = 20, 
                   increment = 3, 
                   command = lambda: print(spin_int.get()),
                   textvariable = spin_int)
                   # from_ = numero inicial, to = numero final, de 3 em 3 (não é simetrico)

spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down'))

#spin['value'] = (1, 2, 3, 4, 5)
spin.pack(pady = 15)


# exercicio
# crie uma spinbox que contenha as letras A B C D E 
# e printe o valor sempre que o valor for decrementado



letras = ('A', 'B', 'C', 'D', 'E') # os itens que aparecerão
letras_srt = tk.StringVar(value = letras[0]) # letra A como padrão
letras_spinbox = ttk.Spinbox(window, textvariable = letras_srt) # criação da spinbox
letras_spinbox['values'] = letras
letras_spinbox.pack()

letras_spinbox.bind('<<Decrement>>', lambda event: print(letras_srt.get()))

#run
window.mainloop()