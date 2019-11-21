import tkinter
from tkinter import *

nomeGlobal = "" #nome do jogador
pontuacaoGlobal = 0
perguntas = open("pergunta1.txt", "r",encoding='latin-1').readlines()
janelaGlobal = None
janelaAviso = None
nomeCaixaTexto = None
indice_resposta = None
respostaSelecionada = None


def validar_nome(event= None):
    global nomeCaixaTexto
    global nomeGlobal
    global janelaGlobal
    
    nomeAtual = nomeCaixaTexto.get() #recebe a string com o nome digitado na caixa de texto de nome 
    if (nomeAtual == ""):
        janelaAviso = Tk()
        janelaAviso.title("Aviso!")
        txt = Label(janelaAviso, text="Nome não pode ficar vazio.", font=("Arial Bold", 10))
        txt.pack()
        bt = Button(janelaAviso, text="Confirmar", command=janelaAviso.destroy)
        bt.pack()
        janelaAviso.mainloop()
    else:
        nomeGlobal = nomeAtual
        janelaGlobal.destroy()
        comecar_quiz()

def comecar_quiz():
    global janelaGlobal 
    
    for pergunta in perguntas:
        exibir_pergunta(perguntas)
    
        
        
        


def exibir_pergunta(linha_pergunta):
    global janelaGlobal 
    global indice_resposta
    global respostaSelecionada

    

    lista = linha_pergunta.split("&")
    txt_pergunta = lista[0]
    

    for i in range(1,len(lista)):
        if(lista[i][0]=="*"):
            lista[i]=lista[i].split("*")[1]
            indice_resposta=i
            break;
    

    janelaGlobal = Tk()
    janelaGlobal.title("Quiz Star Wars")

    respostaSelecionada = IntVar()

    frame_pergunta = Frame(janelaGlobal)
    cabecalho_infos = Frame(janelaGlobal)
    cabecalho_esquerda =Frame(cabecalho_infos)
    cabecalho_direita =Frame(cabecalho_infos)
    
    
    cabecalho_infos.pack(side=TOP, fill=BOTH, expand=1) 
    cabecalho_esquerda.pack(side=LEFT, fill=BOTH, expand=1)
    cabecalho_direita.pack(side=RIGHT, fill=BOTH, expand=1)
    frame_pergunta.pack(side=TOP, fill=BOTH, expand=1)

    
    Label(cabecalho_esquerda, text="Jogando como "+nomeGlobal, font=("Arial Bold", 10)).pack(anchor=NW)
    Label(cabecalho_direita, text="Pontos = " +str(pontuacaoGlobal), font=("Arial Bold", 10)).pack(anchor=E)
    
    Label(janelaGlobal, text="\n"+txt_pergunta+"\n", font=("Arial", 15)).pack()
        
    for i in range(1,len(lista)):
        Radiobutton(janelaGlobal, text=lista[i], variable=respostaSelecionada, value=i).pack(anchor=W)
    
    botaoResposta = Button(janelaGlobal, text="Confirmar", command=resposta).pack()
    #botaoResposta = Button(janelaGlobal, text="Enviar", command=lambda resposta=respostaCaixaTexto.get() :resposta(resposta,lista[indice_resposta],indice_resposta))
    #botaoResposta.pack() 


    janelaGlobal.mainloop()
            
        
def resposta():
    global janelaAviso
    global janelaGlobal
    global pontuacaoGlobal

    if(respostaSelecionada.get()==0):
        janelaAviso = Tk()
        janelaAviso.title("Erro!")
        txt = Label(janelaAviso, text="Escolha uma das opções!", font=("Arial Bold", 10))
        txt.pack()
        bt = Button(janelaAviso, text="Continuar", command=janelaAviso.destroy)
        bt.pack()
        janelaAviso.mainloop()
        
    
    janelaGlobal.destroy()
    if(respostaSelecionada.get()==indice_resposta):
        janelaAviso = Tk()
        janelaAviso.title("Correto!")
        txt = Label(janelaAviso, text="Resposta correta!", font=("Arial Bold", 10))
        txt.pack()
        bt = Button(janelaAviso, text="Continuar", command=janelaAviso.destroy)
        bt.pack()
        janelaAviso.mainloop()
        pontuacaoGlobal=pontuacaoGlobal+10
    else:
        janelaAviso = Tk()
        janelaAviso.title("Errado!")
        txt = Label(janelaAviso, text="Resposta incorreta!", font=("Arial Bold", 10))
        txt.pack()
        bt = Button(janelaAviso, text="Continuar", command=janelaAviso.destroy)
        bt.pack()
        janelaAviso.mainloop()
        
        
        
            
def receber_nome_tela():
    global janelaGlobal
    global nomeCaixaTexto 

    '''
    variavel "janela" recebe uma instancia de Tk(), uma classe do Tkinter, que representa
    a janela principal da interface. Tudo relacionado a coisas da interface
    ou que alteram a interface serão relacionada sempre a ela.
    '''
    janelaGlobal = Tk()

    janelaGlobal.title("Quiz Star Wars") #definindo o titulo da janela principal, "title" é uma variavel interna da classe Tk(), ela já existe lá, apenas estamos mudando seu valor, esse tipo de variavel é chamada de "atributo" em OO, ele é acessado usando [Variavel_da_classe].[atributo]

    #janela.geometry("500x500") #definido o tamanho da tela em pixel



    ''' Agora criaremos oq o tkinter define como "widget" é algo que estará na nossa
    interface, por isso a nossa variavel janela tem que ser passado, pois esse "widget"
    que, neste caso, é um texto de boas vindas pertencerá a uma "janela" principal da interface
    '''
    msgBoasVindas = Label(janelaGlobal, text="Olá, jovem Padawan! Qual o seu nome?", font=("Arial Bold", 20))
    msgBoasVindas.grid(column=0, row=0) #aqui definimos a posição que um widget terá na tela, posicionando como posiçoes de uma matriz por colunas e linhas


    '''Agora criaremos um "widget" que recebe texto que é do tipo Entry, como
    sempre passando a janela principal que ele pertence'''
    nomeCaixaTexto = Entry(janelaGlobal)
    nomeCaixaTexto.grid(column=0, row=1) #definindo a posição na tela, nesse caso abaixo da msg de boas vindas
    nomeCaixaTexto.bind('<Return>', validar_nome)

    '''Agora criaremos um "widget" que é um botão, chamado Button, como
    sempre passando a janela principal que ele pertence, mas nesse caso escolheremos uma
    função que define oq vai ser feito quando o botão for apertado
    nesse caso processar e guardar o nome do usuario'''
    botaoNome = Button(janelaGlobal, text="Enviar", command=validar_nome) #command=FUNÇÃO QUE SERÁ EXE. APOS APERTAR BOTAO
    botaoNome.grid(column=0, row=2) #definindo a posição na tela

    janelaGlobal.mainloop()
    
def exibir_pontos():
    global janelaGlobal

    janelaGlobal = Tk()
    janelaGlobal.title("Quiz Star Wars")
    msgBoasVindas = Label(janelaGlobal, text="FIM DE JOGO,"+nomeGlobal+"! Você fez "+str(pontuacaoGlobal)+" pontos!", font=("Arial Bold", 20))
    msgBoasVindas.grid(column=0, row=0) #aqui definimos a posição que um widget
    botaoNome = Button(janelaGlobal, text="Sair", command=janelaGlobal.destroy) #command=FUNÇÃO QUE SERÁ EXE. APOS APERTAR BOTAO
    botaoNome.grid(column=0, row=2) #definindo a posição na tela
    
receber_nome_tela()
exibir_pontos()
