import tkinter as tk
from tkinter import ttk

#mainframe
window = tk.Tk()
window.title('Menus')
window.geometry('600x400')


#menu (não esquecer do window.configure la em baixo)
menuprincipal = tk.Menu(window)

#submenu
menu_arquivos = tk.Menu(menuprincipal, tearoff = False) #tearoff é para não aparecer a opção ---- que cria uma nova janela no menu
menu_arquivos.add_command(label = 'Novo', command = lambda: print('Novo arquivo'))
menu_arquivos.add_separator()
menu_arquivos.add_command(label = 'Abrir', command = lambda: print('Abrir arquivo'))
menuprincipal.add_cascade(label = 'Arquivos', menu = menu_arquivos)

#submenu de ajuda
ajuda = tk.Menu(menuprincipal, tearoff = False)
ajuda.add_command(label = 'Printa valor do check', command = lambda: print(ajuda_check_string.get()))

ajuda_check_string = tk.StringVar()
ajuda.add_checkbutton(label = 'check', 
                      onvalue = 'on', 
                      offvalue = 'off', 
                      variable = ajuda_check_string) # caixa marcavel

menuprincipal.add_cascade(label = 'Ajuda', menu = ajuda)


#botãoo de menu
menu_botao = ttk.Menubutton(window, text = 'Menu de botão')
menu_botao.pack()

botao_submenu = tk.Menu(menu_botao, tearoff = False)
botao_submenu.add_command(label = 'entry 1', command = lambda: print('teste 1'))
botao_submenu.add_checkbutton(label = 'check 1') # caixa marcavel



#exercicio
#adicionar mais um menu ao menu principal, este deve ter um sub menu

menu_ex = tk.Menu(menuprincipal, tearoff = False)
menu_ex.add_command(label = 'qq coisa')
menuprincipal.add_cascade(label = 'exercicio',  menu = menu_ex)

submenuex = tk.Menu(menu_ex, tearoff = False)
submenuex.add_command(label = 'sub menu do submenu')
menu_ex.add_cascade(label = 'exercicio',  menu = submenuex)

#menu_botao.configure(menu = botao_submenu)
menu_botao['menu'] = botao_submenu # faz o mesmo que o configure

#window.configure(menu = menuprincipal)
window['menu'] = menuprincipal

#run
window.mainloop()