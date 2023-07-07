import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f'x {event.x}, y: {event.y}')

#main frame
window = tk.Tk()
window.title('eventos')
window.geometry('600x500')

#widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window,
                    text = 'Um Simples Botão')
button.pack()

#events
button.bind('<Alt-KeyPress-a>', lambda event: print('evento ocorrido'))
#text.bind('<Motion>', get_pos)    # motion responde a movimentos do mouse
                                    # neste caso, chamei uma função que mapeia a posição do ponteiro na tela, 
                                    # pode ser no frame que eu desejar, seja no window, no text ou em outros...

#window.bind('<KeyPress>', lambda event: print(f'O botão {event.char} foi pressionado'))

entry.bind('<FocusIn>', lambda event: print("O campo de entrada esta selecionado"))
entry.bind('<FocusOut>', lambda event: print("O campo de entrada foi  desselecionado"))
'''  "alt + a" printa no terminal "evento ocorrido"  '''

#                       eventos do tkinter
#  https://www.pythontutorial.net/tkinter/tkinter-event-binding/


# exercicio
# print mousehweel quando o usuário segurar sift e usar a roda do mouse enquanto text esta selecionado

text.bind('<Shift-MouseWheel>', lambda event: print('MouseWheel'))
# em text faça a bind Shift-MouseWheel para o evento print    

#run
window.mainloop()