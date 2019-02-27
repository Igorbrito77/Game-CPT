import pygame, os, random, glob
from pygame.locals import *

class Jogador():

        def __init__(self, tela, tamanho_sprite):
            pygame.sprite.Sprite.__init__(self)

            self.tela = tela
            self.tamanho_sprite = tamanho_sprite
            self.x = 0
            self.y = tela.get_height() - tamanho_sprite
            self.pontuacao = 0
            self.velocidade = 10

            self.ani = glob.glob("personagem/girl/dino_*.png")# carregamos todas as imagens para a animação do sprite
            self.ani.sort()
            self.ani_max = len(self.ani) -1
            self.img = pygame.image.load(self.ani[0])
            self.img_inv = pygame.transform.flip(self.img,True,False)
            self.sprite = self.img
            self.rect = self.sprite.get_rect(center = (self.x, self.y))
            
            self.velocidade_ini_ani = 4
            self.velocidade_ani = self.velocidade_ini_ani
            self.ani_pos = 0
            self.direcao = True
            self.desenha(tela)

        def movimenta(self):
            pos= 0
            tecla = pygame.key.get_pressed()
            if tecla[pygame.K_RIGHT]: 
                pos = 1
            if tecla[pygame.K_LEFT]: 
                pos = -1

            self.rect = self.sprite.get_rect(center = (self.x, self.y)) #atualiza a posição do rect 
            return pos


        def desenha(self, tela): #atualiza a animação do personagem
            imgAux = self.img

            pos = self.movimenta()
            if pos != 0:
                self.x += self.velocidade * pos
                self.velocidade_ani-=1
                if self.velocidade_ani == 0:
                    self.img = pygame.image.load(self.ani[self.ani_pos])
                    self.img_inv = pygame.transform.flip(self.img, True, False)
                    self.velocidade_ani = self.velocidade_ini_ani
                    if self.ani_pos == self.ani_max:
                        self.ani_pos = 0
                    else:
                        self.ani_pos+=1

            if pos == 0:
                if self.direcao:
                    imgAux = pygame.image.load(self.ani[0])
                else:
                    imgAux = pygame.transform.flip(pygame.image.load(self.ani[0]), True, False)

            elif pos == 1:
                imgAux = self.img
                self.direcao = True
            elif pos == -1:
                imgAux = self.img_inv
                self.direcao = False

            tela.blit(imgAux, (self.x, self.y))
        

        def limite_tela(self):
           
            if self.x <0:   self.x = 0
            if self.x >= self.tela.get_width() - self.tamanho_sprite: self.x = self.tela.get_width() - self.tamanho_sprite
