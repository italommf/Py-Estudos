'''
um canvas é um widget que permite voce desenhar formas tais como
quadrados, circulos, linhas, texto, etc

desenhos são feitos através do canvas
'''
import tkinter as tk
from tkinter import ttk

#mainframe
window = tk.Tk()
window.title('caixas de seleção de menu e de rolagem')
window.geometry('600x400')

canvas = tk.Canvas(window, bg = 'white') # bg = background
canvas.pack()

#canvas.create_rectangle((50, 20, 100, 200), #discancia da esquerda, distancia de cima, distancia da direita, distancia do fundo
#                        fill = 'red',
#                        width = 10,
#                        dash = (4, 2, 1, 1),
#                        outline = 'green')

#canvas.create_line(inicio_x, inicio_y, fim_x, fim_y)
#canvas.create_line((0, 0, 150, 200), 
##                  fill = 'blue', 
#                   width = 1)

#canvas.create_oval((200, 0, 300, 100), fill = 'green', outline = 'yellow')

#canvas.create_polygon((0, 0, 100, 200, 300, 50), fill = 'gray')
                     #  x1 y1  x2   y2   x3  y3

#canvas.create_arc((200, 0, 300, 100), fill = 'red', start = 45, extent = 180)

#canvas.create_text((120,220), text = "texto de teste", fill = "green", width = 10)

#canvas.create_window((150,100), window = ttk.Label(window, text = 'este é um texto no canvas'))
#canvas.create_window((150,120), window = ttk.Button(window, text = 'este é um botao no canvas'))

'''
exercicio

use uma bind de evento para criar um app de pintura basico

'''
def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x - brush_size / 2, y - brush_size / 2, x + brush_size / 2, y + brush_size / 2), fill = 'black')
brush_size = 4
canvas.bind('<Motion>', draw_on_canvas)

#run
window.mainloop()