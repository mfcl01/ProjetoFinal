import pygame
from pygame import mixer
pygame.init()
mixer.init()
clock = pygame.time.Clock()
# ----- Gera tela principal
pygame.display.set_caption('Atravesse a Rua!')
window = pygame.display.set_mode((1000, 595))
image = pygame.image.load('assets folder\imagens\Captura de tela 2024-10-30 184033.png')
window.blit(image, (0, 0))
pygame.mixer.music.load('assets\sons\musica lobby.mp3')
pygame.mixer.music.play(-1)
pygame.display.update() 
# ----- Inicia estruturas de dados
colour = (255, 0, 0)
lobby = True
running = True
tela='lobby'

# ===== Loop principal =====
while running:

    if tela == 'lobby':
        window.blit(image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # ----- Verifica consequências
            if event.type == pygame.KEYDOWN:
                    play = True
                    lobby = False
                    pygame.display.update() 
                    tela = 'play'
    if tela == 'play':
        font = pygame.font.SysFont(None, 48)
        text = font.render('HELLO', True, (255, 255, 255))
        text_2 = font.render('WORLD', True, (255, 255, 255))
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                running = False
            if keys[pygame.K_ESCAPE]:
                lobby = True
                play = False
                        
        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador
        pygame.display.flip()
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
