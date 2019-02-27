import pygame, os, random, glob
from pygame.locals import *

class Objeto(pygame.sprite.Sprite):

    def __init__(self, tela, altura, largura):
        pygame.sprite.Sprite.__init__(self)
        self.sorteia()
        self.tela = tela
        self.x = 0
        self.y = 0
        self.altura = altura
        self.largura = largura
        self.na_tela= False
        self.rect = self.sprite.get_rect(center = (self.x, self.y))
        self.libera = False
        

    def cria(self):
        self.x = random.randint(1, self.tela.get_width() - self.largura)
        self.y = self.altura
        self.na_tela = True

    def cai(self, tempo, velocidade):
        self.y += tempo* velocidade

    def desenha(self, tela):
        tela.blit(self.sprite, (self.x, self.y))
        self.rect = self.sprite.get_rect(center = (self.x, self.y))


    def sorteia(self):
        tipo = random.randint(0,5)

        if tipo == 0 or tipo ==2:
            self.tipo = 0
            self.sprite = pygame.image.load("objetos/caveira.png") #carregamos a imagem dos objetos

        elif tipo == 1:
            self.tipo = 1
            self.sprite = pygame.image.load("objetos/chocolate_s.png") #carregamos a imagem dos objetos            
            
        else:
            self.tipo = 2
            self.sprite = pygame.image.load("objetos/bolo.png") #carregamos a imagem dos objetos
                
        
           


