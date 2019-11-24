import random
import time
from pygame import mixer

#lista que contem as perguntas do jogo
lista = ['pergunta1.txt','pergunta2.txt','pergunta3.txt','pergunta4.txt','pergunta5.txt','pergunta6.txt','pergunta7.txt','pergunta8.txt','pergunta9.txt','pergunta10.txt','pergunta11.txt','pergunta12.txt','pergunta13.txt','pergunta14.txt','pergunta15.txt','pergunta16.txt','pergunta17.txt','pergunta18.txt','pergunta19.txt','pergunta20.txt']

pontos = 0

nomeDeUsuario = ''

#vai exibir o ranking na tela
def exibirRanking(lista):
    ran = open('rankingOrdenado.txt','w', encoding='latin-1')
    print('\nVeja qual foi a sua posição no nosso Ranking, Jovem Padawan!\n')
    print('\nCarregando posições no ranking...\n')
    time.sleep(3)
    print('\nSe você estiver entre os 3 primeiros você se tornou um JEDI!!\n')
    time.sleep(3)
    for i in lista:
        print ('\n',i)
        ran.write(i + '\n')
    

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

#função que exibi o as boas vindas ao usuário
def exibir():
    print('\n================================================================================\n')
    print('\n                            Atenção!!!                                          \n')
    print('\n          ***Jogo altamente recomendado para fãs de Star Wars***                \n')
    print('\nResponda as perguntas corretamente e saiba se você pode se tornar um grande Jedi!\n')
    print('\n================================================================================\n')
    time.sleep(7)
    print('\n                    Seja bem vindo jovem padawan!! :D                           \n')
    print('                             \U0001F604', '\U0001F604', '\U0001F604'                 )
    print('\n================================================================================\n')
    print('\n                           Preparado está?                                      \n')
    print('\n================================================================================\n')
    time.sleep(3)

#função que pega o nome do usuário
def cadastrar():
    global nomeDeUsuario
    print('\n================================================================================\n')
    nomeDeUsuario = input('\nDigite Seu nome jovem Padawan: ').upper()
    nomeDeUsuario = nomeDeUsuario.replace(' ', '')
    print('\nPrepare-se para a primeira pergunta',nomeDeUsuario,'que a força esteja com você!\n')
    print('\n================================================================================\n')

#função que cria o ranking
def criarRanking ():
    arquivo = open('ranking.txt', 'a',encoding='latin-1')
    #vai mostrar pontos e nome de usuário
    pU = ' {} {}\n '.format(nomeDeUsuario,pontos)
    arquivo.write(pU)
    arquivo.close()

#função que exibi as perguntas para o usuário e compara a sua resposta
def pergunta(str):
    print('\n===============================================================================\n')
    time.sleep(2)
    arquivo = open(str, 'r',encoding='latin-1')
    arquivo = arquivo.readlines()
    global pontos #para que a função consiga enxergar a várial pontos

    for posiçao, linhas in enumerate(arquivo):
        if posiçao != len(arquivo)-1:
            print(linhas)
        if posiçao == 4:
            resposta = input('Digite sua resposta: \n' ).upper()
            #pequeno tratamento de erros
            while resposta != 'A' and resposta != 'B' and resposta != 'C' and resposta != 'D':
                print('\nResposta inválida jovem padawan, tente novamente\n')
                resposta = input('Digite sua resposta: \n' ).upper()

        if posiçao == 5:
            if resposta in linhas:
                pontos += 100
                musica_acertou()
                print('\nBOAAAAAA Jovem Padawan, VOCÊ ACERTOU!!!\n')
                time.sleep(3)
                musica()
                
            elif resposta not in linhas:
                musica_errou()
                print('\n Que triste Jovem Padawan :(, Você errou!!\n')
                print("\nA resposta correta era:",linhas)
                #print(linhas)
                time.sleep(3)
                musica()
                
    acabou()  

#função que sorteia a pergunta que será exibida para o usuário e pergunta o mesmo deseja continuar jogando
def excutar():
    for i in range(len(lista)):
        #essa variável vai sortear uma pergunta na lista
        nome = random.choice(lista)
        #depois que sorteada a pergunta vai ser removida da lista
        lista.remove(nome)
        #vai chmar a função pergunta exibir na tela
        pergunta(nome)

        sair = input('Digite "ENTER" para continuar e "S" para sair: \n').upper()
        if sair == 'S':
            break
    
        print('\nSeu total de pontos até o momento é:', pontos)

#para o jogo quando as perguntas acabam
def acabou():
    if len(lista) == 0:
        pass

#despedida do usuário
def adeus():
    print(                 '\nAté mais grande jedi!\n'                   )
    time.sleep(3)
    print(             '\n***Que a força esteja com você!***\n'              )
    print('\U0001F590','\U0001F590','\U0001F590','\U0001F590','\U0001F590','\U0001F590')


musica()

exibir()

cadastrar()

excutar()

criarRanking()

ordenaRanking()

adeus()



