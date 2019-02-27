import pygame, time
from classes.objeto import Objeto
from pygame.locals import *

class Fase:

	def __init__(self, objetos, LARGURA_TELA, ALTURA_TELA, velocidade):
		self.objetos = objetos
		self.objetos_na_tela = 0
		self.objetos_fora = 0
		self.max_na_tela = 3
		self.velocidade = velocidade
		self.posicao_limite = 300
		self.LARGURA_TELA = LARGURA_TELA
		self.ALTURA_TELA = ALTURA_TELA
		self.i = 0


	def colisao(self, jogador, objeto):
		if jogador.rect.colliderect(objeto.rect): # se o jogador capturar o objeto, o eliminamos do nosso array e aumentamos a pontuação
			return True



	def queda(self, tela,jogador, tempo,LARGURA_OBJETO, ALTURA_OBJETO):
			#i =0
			#print (len(self.objetos))
			for objeto in self.objetos:  # aqui começa a lógica da queda dos objetos

				if not objeto.na_tela:  #se o objeto ainda não está na tela, chamamos a função que o inicializa
					objeto.cria()
					self.objetos_na_tela += 1

				else:
				    objeto.cai(tempo, self.velocidade) # o objeto continua a sua queda

				objeto.desenha(tela)

				if objeto.y >= self.posicao_limite and not objeto.libera and self.objetos_na_tela < self.max_na_tela:
				    self.objetos.append(Objeto(tela, ALTURA_OBJETO, LARGURA_OBJETO)) # adicionamos outro objeto ao nosso array
				    #print (len(self.objetos))
				    #print("nhhkjhk")
				    objeto.libera = True # booleana que indica que determinado objeto já liberou um objeto seguinte

				if objeto.y >= self.ALTURA_TELA: # se objeto passar do chão, o eliminamos do nosso array
				        self.objetos.remove(objeto) 
				        self.objetos_fora+=1

				if self.colisao(jogador, objeto): # se o jogador capturar o objeto, o eliminamos do nosso array e aumentamos a pontuação
					if objeto.tipo == 0:
						jogador.pontuacao-=10
					elif objeto.tipo == 1:
						jogador.pontuacao +=20
					else:
						jogador.pontuacao += 10
					self.objetos.remove(objeto)
					self.objetos_fora+=1
				
				self.i += 1;

				if(self.i == 3):
				    self.i =0

				if self.objetos_fora == self.max_na_tela: #se todos os objetos foram eliminados, reiniciamos nosso array (com apenas um objeto)
					self.objetos.append(Objeto(tela, ALTURA_OBJETO, LARGURA_OBJETO))
					self.objetos_fora = 0
					self.objetos_na_tela = 0
					self.max_na_tela +=1 # aumentamos o numero de objetos caindo ao mesmo tempo na próxima seção
					self.i = 0
					self.velocidade += (0.05) # aumentamos a velocidade do tempo de queda

	def carrega_tela(self, tela, imagem_fundo,font_ponto, font_nome, pontuacao,segundos):
		tela.fill((0,0,0))
		tela.blit(imagem_fundo, (0,0))
		
		texto_pontos = font_ponto.render("Pontuação: " +str(pontuacao), 1, (9, 255, 255)) 
		tela.blit(texto_pontos, (self.LARGURA_TELA - 250,0))
		texto_tempo = font_ponto.render("Tempo: "+ str(int(segundos)), 1, ((9, 255, 255)))
		tela.blit(texto_tempo, (0,0))
		texto_nome = font_nome.render("Aluno:", 1, ((9, 255, 255)))
		tela.blit(texto_tempo, (0,0))
		

	def exibir_tela_fim(self, tela, jogador, font_ponto, tempo):
		tela.fill((200,0,0))
		texto = font_ponto.render("Fim de jogo!", 1, (255, 200, 255)) 
		tela.blit(texto, (self.LARGURA_TELA/2 - texto.get_width()/2,self.ALTURA_TELA/2 - 3 * texto.get_height()))
		texto = font_ponto.render("Sua pontuação: " +str(jogador.pontuacao), 1, (255, 255, 255)) 
		tela.blit(texto, (self.LARGURA_TELA/2 - texto.get_width()/2,self.ALTURA_TELA/2 - 2 * texto.get_height()))
		texto = font_ponto.render("Parabéns!", 1, (255, 255, 255)) 
		tela.blit(texto, (self.LARGURA_TELA/2 - texto.get_width()/2,self.ALTURA_TELA/2 - 1 * texto.get_height()))
		pygame.display.flip()
		time.sleep(tempo)        