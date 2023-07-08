'''
existem dois tipos de barras no tkinter, deslizantes e de progresso
a deslizante pode ser movida pelo usuário ou setada de forma independente
a barra de progresso somente de forma independente

'''
import tkinter as tk
from tkinter import ttk, scrolledtext

#mainframe
window = tk.Tk()
window.title('caixas de seleção de menu e de rolagem')
window.geometry('600x400')


#slider
scale_int = tk.IntVar(value = 15) # valor padrão definido por mim (posição do deslizador na barra)
scale = ttk.Scale(window, 
                  command = lambda value: print(scale_int.get()), 
                  from_ = 0, 
                  to = 30, 
                  length = 150,
                  orient = 'vertical',
                  variable = scale_int)
                  
scale.pack(pady = 10)


#barra de progresso
progresso = ttk.Progressbar(window, 
                            variable = scale_int, 
                            maximum = 30,
                            orient = 'horizontal',
                            mode = 'indeterminate',
                            length = 100) # maximum é o valor maximo que a barra de status atinge. equivale ao " to "
progresso.pack()
#progresso.start() 

#scrolledtext
scrolled_text = scrolledtext.ScrolledText(window)
scrolled_text.pack()

#run
window.mainloop()