import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('botão com função usando argumentos')
window.geometry('300x200')


def funcao_botao(caixa_input_str):
    print('o botão foi pressionado')
    print(caixa_input_str.get())

#input
caixa_input_str = tk.StringVar(value = 'test')
caixa_input = tk.Entry(window,
                       textvariable = caixa_input_str) # agora "test" fica dentro da caixa de texto
caixa_input.pack()

#botao
botao = tk.Button(window,
                  text = 'Botao Simples',
                  command = lambda: funcao_botao(caixa_input_str))
''' 
command = funcao_botao(caixa_input_str)) executa apenas uma vez. ao pressionar o botão nada acontece pois
a funçã não tem retorno, desta forma o retorno é None.
A forma mais simples de se chamar uma função passando argumentos é atravez de uma função que retorna outra função.
Neste caso utilizamos lambda 

lambda retorna a função "funcao_botao(caixa_input_str)"
'''


botao.pack(pady = 25)

window.mainloop()