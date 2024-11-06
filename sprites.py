import random
import pygame
from pygame.sprite import _Group
from config import LARGURA, ALTURA, LARGURA_DO_CARRO, ALTURA_DO_CARRO, LARGURA_RAPOSA, ALTURA_RAPOSA
from assets import  BACKGROUND, RAPOSA_IMG, WALKING_SOUND, CARRO_IMG, EXPLOSAO_ANIM, load_assets


class Raposa(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[RAPOSA_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA / 2
        self.rect.bottom = ALTURA - 10
        self.speedx = 0
        self.groups = groups
        self.assets = assets
    # Só será possível andar uma vez a cada 500 milissegundos
        self.last_step = pygame.time.get_ticks()
        self.walk_cooldown = 500
    
    def update(self):
    # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.up > 0:
            self.rect.up = 0
        if self.rect.up > ALTURA:
            self.rect.up = ALTURA
    def walk(self):
        # Verifica se pode andar
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último passo.
        elapsed_ticks = now - self.last_step

        # Se já pode andar novamente...
        if elapsed_ticks > self.walk_cooldown:
            # Marca o tick da nova imagem.
            self.last_step = now
            # A nova bala vai ser criada logo acima e no centro horizontal da nave

            self.assets[WALKING_SOUND].play()

class Carro(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[CARRO_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, LARGURA-LARGURA_DO_CARRO)
        self.rect.y = random.randint(-100, -ALTURA_DO_CARRO)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)
class Background(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[BACKGROUND]
        self.rect = self.image.get_rect()
        self.rect.x = 
        self.rect.y = 
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)