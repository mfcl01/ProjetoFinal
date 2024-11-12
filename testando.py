import pygame
import sys
from pygame import mixer
import assets
import config
from sprites import *
import sprite_ajuda

pygame.init()
mixer.init()
clock = pygame.time.Clock()
# ----- Gera tela principal
pygame.display.set_caption('Atravesse a Rua!')
largura, altura = pygame.display.Info().current_w, pygame.display.Info().current_h

window = pygame.display.set_mode((500, 500))
pygame.display.update() 

# Condições Iniciais
lobby = True
running = True
tela ='lobby'


# Sprite Raposa teste
sprite_raposa_image = pygame.image.load("FOXSPRITESHEET.png").convert_alpha()
sprite_sheet = sprite_ajuda.SpriteSheet(sprite_raposa_image)
BLACK = (0,0,0)

def pegar_imagem(sheet, frame, width, height, scale):
    image = pygame.Surface((width,height), pygame.SRCALPHA).convert_alpha()
    image.blit(sheet,(0, 0), ((frame *  width), 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    return image 


# Acoes
idle_frontal = 0
idle_direita = 1
idle_esquerda = 2
idle_atras = 3
frontal = 4
direita = 5
esquerda = 6
atras = 7
correr_abaixo = 8
correr_esquerda = 9 
correr_direita = 10 
correr_cima = 11

# Lista de animação
lista_animacao = []
animacao_passos = [4,4,4,4,1,1,1,1,8,8,8,8]
last_update = pygame.time.get_ticks()

acao = 0




animacao_tempo_espera = 100
frame = 0
contador_passo = 0

for animacao in animacao_passos:
    img_temp_lista = []
    for _ in range(animacao):
        img_temp_lista.append(sprite_sheet.pegar_imagem(contador_passo,32,32,3))
        contador_passo += 1
    lista_animacao.append(img_temp_lista)






# ===== Loop principal =====
while running:
    window.fill((200,0,0))
    # Mudar animacao
    tempo_agora = pygame.time.get_ticks()
    if tempo_agora - last_update >= animacao_tempo_espera:
        frame += 1
        last_update = tempo_agora
        if frame >= len(lista_animacao[acao]):
            frame = 0

    window.blit(lista_animacao[acao][frame],(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and acao > 0:
                acao -= 1
                frame = 0
            if event.key == pygame.K_UP and acao < len(animacao_passos)-1:
                acao += 1
                frame = 0
            

        
    pygame.display.flip()
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados