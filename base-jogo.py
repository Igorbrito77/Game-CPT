import pygame, os, random, glob, time
from pygame.locals import *
from classes.jogador import Jogador
from classes.objeto import Objeto
from classes.fase import Fase

pygame.init()

LARGURA_TELA = 1000
ALTURA_TELA = 600
TAMANHO_SPRITE = 150
ALTURA_OBJETO = 60
LARGURA_OBJETO = 60

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
os.environ['SDL_VIDEO_WINDOW_POS'] = "200,0" # posição da janela na tela
pygame.display.set_caption('Game Computação para Todos') #titulo da janela


pygame.font.init()
font_padrao = pygame.font.get_default_font() # fonte do texto
font_ponto = pygame.font.SysFont("comicsansms", 45)# prepara o texto para a pontuação
font_nome  = pygame.font.SysFont(font_padrao, 45)

fim = False
clock = pygame.time.Clock()
tempo = clock.tick(80)
velocidade = 0.5

imagem_fundo = pygame.image.load("fundo/castelo.png") # carrega a imagem de fundo do game

jogador = Jogador(tela, TAMANHO_SPRITE)
objetos = []
objetos.append(Objeto(tela, ALTURA_OBJETO, LARGURA_OBJETO))
objetos[0].caiu = False

fase = Fase(objetos, LARGURA_TELA, ALTURA_TELA, velocidade)

segundos = 0 

while not fim and segundos < 100:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim = True
        
        segundos = pygame.time.get_ticks()/1000
        fase.carrega_tela(tela, imagem_fundo, font_ponto, font_nome, jogador.pontuacao,segundos) # função que carrega os sprites na tela

        fase.queda(tela, jogador, tempo, ALTURA_OBJETO, LARGURA_OBJETO)

        jogador.desenha(tela)
        jogador.limite_tela()

        pygame.display.flip()
        clock.tick(60)

fase.exibir_tela_fim(tela, jogador, font_ponto, 3) #exibe a tela de fim de jogo por 3 segundos
pygame.quit()
