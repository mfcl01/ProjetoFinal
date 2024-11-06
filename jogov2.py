import pygame
from pygame import mixer
pygame.init()
mixer.init()
clock = pygame.time.Clock()
# ----- Gera tela principal
pygame.display.set_caption('Atravesse a Rua!')
largura, altura = pygame.display.Info().current_w, pygame.display.Info().current_h
window = pygame.display.set_mode((largura, altura), pygame.FULLSCREEN)
image_lobby = pygame.image.load('Captura de tela 2024-10-30 184033.png')
image_lobby = pygame.transform.scale(image_lobby, (largura, altura))
rua = pygame.image.load('rua.jpeg')
rua = pygame.transform.scale(rua, (largura, altura))
window.blit(image_lobby, (0, 0))
pygame.mixer.music.load('assets\sons\musica lobby.mp3')
pygame.mixer.music.play(-1)
pygame.display.update() 

# ----- Inicia estruturas de dados
colour = (255, 0, 0)
lobby = True
running = True
tela ='lobby'
raposa = pygame.image.load('raposa.webp')
x, y = 0, 0
velocidade = 0.1   # Quantos pixels o personagem se move por frame

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
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if keys[pygame.K_UP]:
            y += velocidade
        if keys[pygame.K_DOWN]:
            y -= velocidade
        if y < 0:
            y = 0

        # ----- Atualiza estado do jogo
        window.fill((0, 0, 0))  # Limpa a tela para não deixar rastros
        window.blit(rua, (x, y))  # Desenha o personagem na nova posição
        pygame.display.update()  # Mostra o novo frame para o jogador
        pygame.display.flip()
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
