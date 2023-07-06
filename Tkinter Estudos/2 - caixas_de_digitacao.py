from cProfile import label
import tkinter as tk 
from tkinter import ttk

def funcao_botao():
    texto_digitado = entrada_str.get()
    saida_str.set(texto_digitado)

    texto['text'] = 'novo texto da label' # muda o texto da labem texto
    entrada['state'] = 'disable' # trava a edição do campo de entrada linha
    # print(texto.configure()) # mostra todas as configs possiveis para o metodo configure

def reseta_label_texto():
    entrada['state'] = 'enabled'

# janela principal
janela = tk.Tk()
janela.title('Janela e widgets')
janela.geometry('800x600')

'''implementar saida'''
# janela de digitação
tk.Text(master = janela).pack(pady = 10) # pady controla a posição vertical da janela de texto 

# texto na tela abaixo da caixa grande

texto_novo = tk.StringVar()

texto = ttk.Label(master = janela, text = 'teste', textvariable = texto_novo)
texto.pack()

# entrada (input)
entrada_str = tk.StringVar() # entrada caixa linha
entrada = ttk.Entry(master = janela, textvariable = texto_novo) # caixa de texto (linha unica)
entrada.pack(pady = 10) 

# botão
botao = ttk.Button(master = janela, text = 'texto do botão', command = funcao_botao)
botao.pack(pady = 10)

# botão reseta config 
botao2 = ttk.Button(master = janela, text = 'botao reseta label', command = reseta_label_texto)
botao2.pack(pady = 10)

# saida_botao
saida_str = tk.StringVar()
saida = tk.Label(master = janela, text = 'saida', textvariable = saida_str)
saida.pack()

# run
janela.mainloop()