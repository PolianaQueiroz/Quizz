from tkinter import* 

def exibir():
    lab['text'] = 'Responda as perguntas corretamente e saiba se você pode se tornar um grande Jedi'
    

janela = Tk()
janela.title('Quizz Star Wars')
janela['bg'] = 'blue' #cor da janela

janela.geometry('800x600+100+50')

lab = Label(janela, text = 'Seja bem vindo jovem padawan!!')
lab.place(x=250, y=250) #dimenssões do texto na janela

#criando botão na tela
bt = Button(janela, width = 20, text = 'continuar', command =  exibir)
bt.place(x=280, y=450) #dimenssões do botão na janela



#a janela fica aberta até que o usuário a feche
janela.mainloop()