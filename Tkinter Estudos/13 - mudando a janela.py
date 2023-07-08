'''
ate agora mudamos apenas o tamanho e o nome da janela
Nós podemos mudar a opacidade, a posição, full screen, barra de título e muito mais

'''

import tkinter as tk
from tkinter import ttk






#mainframe
window = tk.Tk()
window.title('caixas de seleção de menu e de rolagem')

largura = 600
altura = 400

largura_monitor = window.winfo_screenwidth()
altura_monitor = window.winfo_screenheight()

largura_monitor_inicio = int((largura_monitor / 2) - (largura/2))
altura_monitor_inicio = int((altura_monitor / 2) - (altura/2))

window.geometry(f'{largura}x{altura}+{largura_monitor_inicio}+{altura_monitor_inicio}') # largura, altura, distancia da esquerda, distancia de cima
window.iconbitmap('C:/Users/warfa/OneDrive/Documentos/Italo/Curso/Tkinter Estudos/ico/icone-pc.ico')

#tamanhos da janela
window.minsize(500, 300) # tamanho minimo
#window.maxsize(700, 500) # tamanho maximo, desativado por causa do fullscreen
window.resizable(True, True) # aumentar nas direções: X, Y

print(window.winfo_screenwidth())
print(window.winfo_screenheight())

#atribulos de window
window.attributes('-alpha', 0.9) # transparencia, vai de 0 a 1
window.attributes('-topmost', True) # nunca sobreposta

#evento de segurança
window.bind('<Escape>', lambda event: window.quit()) # esc fecha a janela, alguns 

#window.attributes('-disable', False) # True para desativar a janela, só fecha pelo esc definido acima
window.attributes('-fullscreen', False) # Fica sem os botões de fechar, usa o botão ESC de emeregencia definido acima

#title bar (barrinha de cima do programa)
window.overrideredirect(False) # True oculta a title bar
grip = ttk.Sizegrip(window)
grip.place(relx = 1.0, rely = 1.0, anchor = 'se') # x e y aqui funcionam como no plano cartesiano





#exercicio
# fazer a janela começar no meio da tela


#run
window.mainloop()