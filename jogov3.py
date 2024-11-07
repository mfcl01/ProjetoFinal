import pygame
from pygame import mixer
import assets
pygame.init()
mixer.init()
clock = pygame.time.Clock()
# ----- Gera tela principal
pygame.display.set_caption('Atravesse a Rua!')
largura, altura = pygame.display.Info().current_w, pygame.display.Info().current_h
window = pygame.display.set_mode((largura, altura), pygame.FULLSCREEN)
image_lobby = pygame.image.load('Captura de tela 2024-10-30 184033.png')
image_lobby = pygame.transform.scale(image_lobby, (largura, altura))
window.blit(image_lobby, (0, 0))
pygame.mixer.music.load('musica lobby.mp3')
pygame.mixer.music.play(-1)
pygame.display.update() 

# ----- Inicia estruturas de dados
rua = pygame.image.load('rua.jpeg')
rua = pygame.transform.scale(rua, (largura, altura))
rua2 = pygame.image.load('rua.jpeg')
rua2 = pygame.transform.scale(rua2, (largura, altura))
lobby = True
running = True
tela ='lobby'
#raposa = pygame.image.load('raposa.webp')

carro_img = pygame.image.load('Carro azul.png').convert_alpha()
carro = pygame.transform.scale(carro_img, (assets.LARGURA_DO_CARRO, assets.ALTURA_DO_CARRO))

carro_x = -10
carro_y = 500
carro_speed = 2.5
x, y = 0, 0
y2 = 1000
velocidade = 5   # Quantos pixels o personagem se move por frame

# ===== Loop principal =====
while running:

    if tela == 'lobby':
        window.blit(image_lobby, (x, y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # ----- Verifica consequências
            if event.type == pygame.KEYDOWN:
                    tela = 'play'
                    pygame.display.update() 

    if tela == 'play':
        font = pygame.font.SysFont(None, 48)
        window.blit(rua, (x, y))
        window.blit(rua2, (x, y2))
        keys = pygame.key.get_pressed()
        carro_x += carro_speed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if keys[pygame.K_UP]:
            y += velocidade
            y2 += velocidade
            carro_y += velocidade
        if keys[pygame.K_DOWN]:
            y -= velocidade
            y2 -= velocidade 
            carro_y -= velocidade
        if y < 0:
            y = 0
            y2 = 1000
            carro_y = 500
        if y >= altura:
            y = -altura
            carro_y = 500
        if y2 >= altura:
            y2 = -altura
        if carro_x + assets.LARGURA_DO_CARRO < 0 or carro_x > largura:
            carro_x = -10

        # ----- Atualiza estado do jogo
        window.fill((0, 0, 0))  # Limpa a tela para não deixar rastros
        window.blit(rua, (x, y))  # Desenha o mapa na nova posição
        window.blit(rua2, (x, y2))
        window.blit(carro, (carro_x, carro_y))
        pygame.display.update()  # Mostra o novo frame para o jogador
        pygame.display.flip()
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados