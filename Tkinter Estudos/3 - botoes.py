import tkinter as tk
from tkinter import ttk

''' existem 3 tipos majoritarios de botão: botões, caixas de marcação (checkbox) e radio button (o de escolha redondo)'''

# main frame
janela = tk.Tk()
janela.title('botoes')
janela.geometry('640x480')

# botao simples
'''
def botao_funcao():
    print('Botao básico')

substituí pela função lambda
'''
botao_str = tk.StringVar(value = 'botao com string var') # ao definir uma variavel do tk ao botão, o valor dela sobrescreve o texto do botão
botao = ttk.Button(janela, 
                   text = 'Botão simples e comum', 
                   command = lambda: print('botao simples'), 
                   textvariable = botao_str)
botao.pack()

# botao caixa de marcação
check_var = tk.IntVar(value = 10) # como 10 e o valor de onvalue, a caixa por padrão ja começa marcada, caso 5, desmarcada
check = ttk.Checkbutton(janela, 
                        text = 'checkbox 1', 
                        command = lambda: print(check_var.get()),
                        variable = check_var, # esta marcado ou não, retorna 1 ou 0, pode ser intvar, stringvar, booleanvar, depende do que voce quer.
                        onvalue = 10, # quando marcado, o valor é 10
                        offvalue = 5) # quando desmarcado, o valor é 5
check.pack()  

# botao redondo
'''   botao redondo 1 me da o 'value' do botao em redondo1_var   '''
redondo1_var = tk.StringVar()
redondo1 = ttk.Radiobutton(janela, 
                           text = "botao redondo 1",
                           value = 'redondo1', # pode ser qualquer valor, contando que seja diferente do segundo
                           command = lambda: print(redondo1_var.get()),
                           variable = redondo1_var)
redondo1.pack()

'''   botao redondo 2 me da o 'text' do botao   '''
redondo2 = ttk.Radiobutton(janela, 
                           text = "botao redondo 2",
                           value = 'redondo2', # pode ser qualquer valor, contando que seja diferente dos outros
                           command = lambda: print('botao redondo 2'))                          
redondo2.pack()                               

#run
janela.mainloop()