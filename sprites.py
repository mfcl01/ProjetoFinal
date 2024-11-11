import random
import pygame
from pygame.sprite import Group
from config import LARGURA, ALTURA, LARGURA_DO_CARRO, ALTURA_DO_CARRO, LARGURA_RAPOSA, ALTURA_RAPOSA
from assets import  BACKGROUND, RAPOSA_IMG, WALKING_SOUND, CARRO_IMG, EXPLOSAO_ANIM, load_assets


class Raposa(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = 1536 / 2
        self.rect.bottom = 680
        self.speedx = 0
        
    
    def update(self):
    # Atualização da posição da raposa
        self.rect.x += self.speedx
        self.rect.x -= self.speedx

        # Mantem dentro da tela
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0

    def reset_x(self):
        self.rect.x = 0

    def reset_y(self):
        self.rect.y = self.starty

    def aumenta_velocidade(self):
        self.speedx *= 5

class Carro(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speedx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.startx = x
        self.rect.y = y
        self.starty = y
        self.speedx = speedx
    
    def update(self):
        self.rect.x += self.speedx
        if self.speedx < 0:
            if self.rect.x + self.rect.width < 0:
                self.rect.x = self.startx
        else:
            if self.rect.x > pygame.display.Info().current_w:
                self.rect.x = self.startx
    
    def reset_x(self):
        self.rect.x = self.startx

    def reset_y(self):
        self.rect.y = self.starty

    def aumenta_velocidade(self):
        self.speedx *= 1.02

class Background(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.starty = y

    def update(self):
        pass

    def reset_x(self):
        self.rect.x = 0

    def reset_y(self):
        self.rect.y = self.starty