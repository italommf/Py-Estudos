import tkinter as tk
from tkinter import ttk

# funcao a ser chamada no pressionar do botao
def minha_funcao_conversora():
    milhas_input = entrada_int.get() # .get() captura o dado de entrada_int (variavel do botão)
    km_output = milhas_input * 1.61
    saida_string.set(km_output) # saida_string é a variavel de saida setada no frame em saida, .set() seta o valor da variavel passada como parametro
    



# Janela principal

janela = tk.Tk()
janela.title('Conversor de Milhas para km') # texto da barra de titulo
janela.geometry('400x200') # tamanho da janela principal

# Texto da janela (dentro)
titulo_app = ttk.Label(master = janela,
                       text = 'Milhas para Quilômetros',
                       font = 'Calibri 24 italic bold')
                        #  fonte tamanho estilo
titulo_app.pack()

# Campo de input
janela_input = ttk.Frame(master = janela) # o frame que contem os dois widgets abaixo, botão e caixa de texto       

entrada_int = tk.IntVar() # variavel do tk para armazenar o valor de "entrada"
entrada = ttk.Entry(master = janela_input, textvariable = entrada_int) # caixa de texto dentro de janela_input

botao = ttk.Button(master = janela_input, text = 'Converter', command = minha_funcao_conversora) # botão dentro de janela_input
entrada.pack(side = 'left', padx = 10) # distancia entre os dois widgets (botão e caixa de input)
botao.pack(side = 'left') 
janela_input.pack(pady = 10) # distancia entre o widget de texto (label) e o frame que contem o botão e a caixa de input

# saida de dados
saida_string = tk.StringVar()
saida = ttk.Label(master = janela,
                  text = 'saida',
                  font = 'Calibri 20 italic',
                  textvariable = saida_string
                  )
saida.pack(pady = 25)

# Rodando a janela com os widgets
janela.mainloop()

