from tkinter import* 

janela = Tk()
janela.title('Quizz Star Wars')
janela['bg'] = 'blue' #cor da janela

janela.geometry('800x600+100+50')

lab = Label(janela, text = '  Seja bem vindo jovem padawan!!  ')
lab.place(x=250, y=250)

#a janela fica aberta até que o usuário a feche
janela.mainloop()