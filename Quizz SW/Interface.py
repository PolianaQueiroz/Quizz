import random, time
from tkinter import *
from pygame import mixer

#lista que contem as perguntas do jogo
listadePerguntas = ['pergunta1.txt','pergunta2.txt','pergunta3.txt','pergunta4.txt','pergunta5.txt','pergunta6.txt','pergunta7.txt','pergunta8.txt','pergunta9.txt','pergunta10.txt','pergunta11.txt','pergunta12.txt','pergunta13.txt','pergunta14.txt','pergunta15.txt','pergunta16.txt','pergunta17.txt','pergunta18.txt','pergunta19.txt','pergunta20.txt']

pontos = 0
usuario = ''

#função para rodar a música enquanto o usuário joga
def musica():
    mixer.init()
    mixer.music.load('musica.mp3')
    mixer.music.play()

#função para tocar musica quando o usuário acertar
def musica_errou():
    mixer.init()
    mixer.music.load('Errou.mp3')
    mixer.music.play()

#função paratocar musica quando acertar
def musica_acertou():
    mixer.init()
    mixer.music.load('acertoumiseravel.mp3')
    mixer.music.play()

# construindo a minha janelinha e nomeando a minha janela com o nome do meu jogo
def construtor():
    global janela,ima

    musica()

    janela = Tk()
    janela['bg'] = 'red' # cor de fundo
    janela.title('Star Wars Quizz')

    imagem = PhotoImage(file='stj.png') #inserindo imagem na tela inicial
    ima = Label(janela, image = imagem)
    ima.image = imagem
    ima.pack()

    janela.geometry('1260x690')

def menu():
    global btinicio,btranking,btIntrucao,btSair1

    btinicio = Button(text='Iniciar Jogo', command= pegar_nome)
    btinicio.place(x=780, y=450)
   
    
    btranking = Button(text='Ranking', command= ordenaRanking)
    btranking.place(x=780, y=500)

    btinstrucao  = Button(text='Instruções', command=instrucao)
    btinstrucao.place(x=780, y=550)

    btSair1  = Button(text='Sair', command=janela.destroy)
    btSair1.place(x=780, y=600)


#destrui botões depois que o usuario clicar
def iniciar_jogo():
    global btinicio,btranking

    #btinicio.destroy()
    #btranking.destroy()
    ima.destroy()
    musica()
    exibir_pergunta()
    pergunta()

def instrucao():
    janela.destroy()

    global lblinstrucao, jinstrucao
    jinstrucao = Tk()
    jinstrucao.title('Intruções!')

    arquivo = open('Instrucao.txt', 'r',encoding='latin-1')
    arquivo = arquivo.readlines()
        
    lblinstrucao = Label(jinstrucao,text=arquivo,font='Arial 20')
    lblinstrucao.pack()

    btacessar = Button(jinstrucao, text = 'Iniciar Jogo', command=sairIntrucao)
    btacessar.pack()

    jinstrucao.mainloop()

    #construtor()
    #iniciar_jogo()

def setaValorPontuacao(lbl):
    lbl['text'] = "Valor Acumulado: " +str(pontos)


def exibir_pergunta():
    global lblpontuacao
    global lblpergunta
    global btA, btB, btC, btD, btSair
    
    
    lblpergunta = Label(text='',font='Arial 20')
    lblpergunta.pack()
    lblpontuacao = Label(text= 'Total de pontos: '+str(pontos))
    lblpontuacao.pack()

    btA = Button(text='A', command = lambda: verificar_resposta('A')) #width=10, height=7)
    btA.place(x=500, y=600)

    btB = Button(text='B', command = lambda: verificar_resposta('B'))
    btB.place(x=600, y=600)

    btC = Button(text='C', command = lambda: verificar_resposta('C'))
    btC.place(x=700, y=600)

    btD = Button(text='D', command = lambda: verificar_resposta('D'))
    btD.place(x=800, y=600)

    btSair  = Button(text='Sair', command = lambda: destrui_tudo())
    btSair.place(x=650, y=650)

def sortear_pergunta():
    #essa variável vai sortear uma pergunta na lista
    nome = random.choice(listadePerguntas)
    #depois que sorteada a pergunta vai ser removida da lista
    listadePerguntas.remove(nome)
    #vai chmar a função pergunta exibir na tela
    return nome 


#função que exibi as perguntas para o usuário e compara a sua resposta
def pergunta():
    if len(listadePerguntas) == 0:
        destrui_tudo()
        criarRanking()

    else:
        nomePergunta = sortear_pergunta()

        arquivo = open(nomePergunta, 'r',encoding='latin-1')
        arquivo = arquivo.readlines()
        global pontos, respCorreta #para que a função consiga enxergar a várial 
        
        minhaPergunta = ''

        for posiçao, linhas in enumerate(arquivo):
            if posiçao != len(arquivo)-1:
                minhaPergunta += '{}\n'.format(linhas)

            if posiçao == 5:
                respCorreta = linhas
        
        #print(respCorreta)            
        lblpergunta['text'] = minhaPergunta
        lblpontuacao['text'] = "Total de Pontos: " +str(pontos)

#caso as perguntas acabem tudoque esta sendo exibido na janela vai ser destruido
def destrui_tudo():
    janela.destroy()
    construtor() 
    menu()

#se usuario acertar toca a música e exbir uma nova pergunta
def verificar_resposta(resp):
    global pontos
    
    if respCorreta == resp:
        pontos += 100
        musica_acertou()
        pergunta()
        
        
    else:
        musica_errou()
        time.sleep(2)
        destrui_tudo()
        
        #construtor()
       
        #armazena o nome e os pontos no arquivo de ranking
        criarRanking()
       

def pegar_nome():
    #destroi a janela
    janela.destroy()

    jusuario = Tk()
    jusuario.title('Cadastro de Usuário')
    #jusuario.geometry('400x500')

    #pega o usuario que esta na caixa de texto
    def get_user():
        user = tbNome.get()
    

        if tbNome == '':
            pass

        else:
            #armazena o usuario que está jogando
            global usuario
            usuario = user

            #distroi a janel e inicia o jogo
            jusuario.destroy()
            
            construtor()
            iniciar_jogo()

    #cria as labels com o nome, campo para o nome e botão de acessar
    lblnome = Label(jusuario, text = 'Digite seu nome:')
    lblnome.pack()

    tbNome = Entry(jusuario)
    tbNome.pack()

    btacessar = Button(jusuario, text = 'Iniciar Jogo', command=get_user)
    btacessar.pack()

    jusuario.mainloop()

#função que cria o ranking
def criarRanking ():
    arquivo = open('ranking.txt', 'a',encoding='latin-1')
    #vai mostrar pontos e nome de usuário
    pU = '{} {}\n'.format(usuario,pontos)
    arquivo.write(pU)
    arquivo.close()

def exibirRanking(listaOrdenados):
    #print(listaOrdenados)
    janelaRanking = Tk()
    janelaRanking.title('RANKING')

    meuRanking = Label(janelaRanking, text='')
    meuRanking.pack()

    def exibir():
        pessoas = ''
        for pos, i in enumerate(listaOrdenados):
            if pos < 10:
                pessoas += '{}° -- {}\n'.format((pos+1), i)

        meuRanking['text'] = pessoas

    exibir()
    janelaRanking.mainloop()

def sairIntrucao(): 
    jinstrucao.destroy()
    construtor()
    menu()

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
    
    exibirRanking(listaOrdenados)

construtor()

menu()

janela.mainloop()

