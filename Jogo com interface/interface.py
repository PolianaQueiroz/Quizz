import random
import time
import tkinter
from tkinter import *
from pygame import mixer

nomeGlobal = "" #nome do jogador
pontuacaoGlobal = 0
perguntas = open("perguntas.txt", "r", encoding= 'latin-1').readlines()
janelaGlobal = None
janelaAviso = None
nomeCaixaTexto =None
indice_resposta =None
respostaSelecionada =None
textoRanking = None


#vai retorna o ranking já ordenado
def exibirRanking(lista):
    texto = ''
    ran = open('rankingOrdenado.txt','w', encoding='latin-1')
    texto+='\nVeja qual foi a sua posição no nosso Ranking, Jovem Padawan!\n'
    texto+='\nSe você estiver entre os 3 primeiros você se tornou um JEDI!!\n'
    time.sleep(3)
    for i in lista:
        texto+='\n'+i
        ran.write(i + '\n')
    return texto

#função que ordena a pontuação do ranking
def ordenaRanking():
    listaOrdenados = []
    desordenados = open('ranking.txt','r',encoding='latin-1')
    desordenados = desordenados.read()
    lista = desordenados.split()

    while len(lista) != 0:
        maior = 0
        indice = 0
        for i in range(len(lista)):
            if not (i % 2 == 0):
                if int(lista[i]) > maior:
                    maior = int(lista[i])
                    indice = i
        listaOrdenados.append(lista[indice-1]  + ' - ' +  lista[indice] ) 
        del lista[indice]
        del lista[indice-1]
    return exibirRanking(listaOrdenados)

#função que cria o ranking
def criarRanking ():
    arquivo = open('ranking.txt', 'a',encoding='latin-1')
    #vai mostrar pontos e nome de usuário
    pU = ' {} {}\n '.format(nomeGlobal,pontuacaoGlobal)
    arquivo.write(pU)
    arquivo.close()


#função para rodar a música enquanto o usuário joga
def musica():
    mixer.init()
    mixer.music.load('musica.mp3')
    mixer.music.play()





def validar_nome(event=None):
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
        exibir_pergunta(pergunta)
    
        
        
        


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

    janelaGlobal.title("Quiz Star Wars") #definindo o titulo da janela principal, "title" é uma variavel interna da classe Tk(), ela já existe lá, apenas mudei seu valor/atributo

    #janela.geometry("500x500") #definido o tamanho da tela em pixel



    msgBoasVindas = Label(janelaGlobal, text="Olá, jovem Padawan! Qual o seu nome?", font=("Arial Bold", 20))
    msgBoasVindas.grid(column=0, row=0) #aqui definimos a posição que um widget terá na tela, posicionando como posiçoes de uma matriz por colunas e linhas


    nomeCaixaTexto = Entry(janelaGlobal)
    nomeCaixaTexto.grid(column=0, row=1) #definindo a posição na tela, nesse caso abaixo da msg de boas vindas
    nomeCaixaTexto.bind('<Return>', validar_nome)

    
    botaoNome = Button(janelaGlobal, text="Enviar", command=validar_nome) #command=FUNÇÃO QUE SERÁ EXE. APOS APERTAR BOTAO
    botaoNome.grid(column=0, row=2) #definindo a posição na tela

    janelaGlobal.mainloop()
    
def exibir_pontos():
    global janelaGlobal

    janelaGlobal = Tk()
    janelaGlobal.title("Quiz Star Wars")
    msgBoasVindas = Label(janelaGlobal, text="FIM DE JOGO,"+nomeGlobal+"! Você fez "+str(pontuacaoGlobal)+" pontos!", font=("Arial Bold", 20))
    msgBoasVindas.grid(column=0, row=0) #aqui definimos a posição que um widget
    
    Ranking = Label(janelaGlobal, text=textoRanking, font=("Arial Bold", 20))
    Ranking.grid(column=0, row=1)
    botaoNome = Button(janelaGlobal, text="Sair", command=janelaGlobal.destroy) #command=FUNÇÃO QUE SERÁ EXE. APOS APERTAR BOTAO
    botaoNome.grid(column=0, row=2) #definindo a posição na tela

#chamando as funções
musica()    
receber_nome_tela()
criarRanking()
textoRanking = ordenaRanking()
exibir_pontos()

