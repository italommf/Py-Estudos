'''
Frame é um widger vazio, voce coloca outros widgets dentro do frame
é a forma mais facil de arranjar outros widgets
* frames são "invisíveis"
'''

import tkinter as tk
from tkinter import ttk

#mainframe
window = tk.Tk()
window.title('Frames')
window.geometry('600x400')

#frame
frame = ttk.Frame(window, width = 150, height = 200, borderwidth = 10, relief = tk.GROOVE)
frame.pack_propagate(False) # faz com que o tamanho definido no frame seja o tamanho usado e não o tamanho apenas dos widgets dentro do frame
frame.pack(side = 'left')



#parentting (master settings)
label = ttk.Label(frame, text = 'Label no frame')
label.pack()

botao = ttk.Button(frame, text = 'botao no frame')
botao.pack()

# exemplo
label2 = ttk.Label(window, text = 'label fora do frame')
label2.pack(side = 'left')


#exercicio

#frame 2 (exercicio)
frame2 = ttk.Frame(window, width = 150, height = 200, borderwidth = 10)
frame2.pack_propagate(True) 
frame2.pack(side = 'left')

label2 = ttk.Label(frame2, text = 'Label no frame')
label2.pack()

botao2 = ttk.Button(frame2, text = 'botao no frame')
botao2.pack()

entry = ttk.Entry(frame2)
entry.pack()

 
#run
window.mainloop()