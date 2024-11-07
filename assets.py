import pygame
import os
from config import LARGURA_DO_CARRO, ALTURA_DO_CARRO, LARGURA_RAPOSA, ALTURA_RAPOSA, IMG, SND, LARGURA_CAMINHAO, ALTURA_CAMINHAO

BACKGROUND = 'background'
CARRO_IMG = 'carro_img'
CARRO_IMG = 'carro_img'
RAPOSA_IMG = 'raposa_img'
RAPOSA_IMG = 'raposa_img'
EXPLOSAO_ANIM = 'explosao_anim'
SCORE_FONT = 'score_font'
DEATH_SOUND = 'death_sonud'
WALKING_SOUND = 'walking_sound'
CAMINHAO_IMG = 'caminhao_img'
def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG, 'starfield.png')).convert()
    assets[CARRO_IMG] = pygame.image.load(os.path.join(IMG, 'meteorBrown_med1.png')).convert_alpha()
    assets[CARRO_IMG] = pygame.transform.scale(assets['carro_img'], (LARGURA_DO_CARRO, ALTURA_DO_CARRO))
    assets[RAPOSA_IMG] = pygame.image.load(os.path.join(IMG, 'playerShip1_orange.png')).convert_alpha()
    assets[RAPOSA_IMG] = pygame.transform.scale(assets['ship_img'], (LARGURA_RAPOSA, ALTURA_RAPOSA))
    EXPLOSAO_ANIM = []
