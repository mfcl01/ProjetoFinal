import pygame
from pygame import mixer
pygame.init()
mixer.init()
clock = pygame.time.Clock()
# ----- Gera tela principal
pygame.display.set_caption('Atravesse a Rua!')
window = pygame.display.set_mode((800, 600))
image = pygame.image.load("assets folder/imagens/Captura de tela 2024-10-30 184033.png")
image = pygame.image.load('Captura de tela 2024-10-30 184033.png')
window.blit(image, (0, 0))
pygame.mixer.music.load('musica lobby.mp3')
pygame.mixer.music.play(-1)
pygame.display.update() 
# ----- Inicia estruturas de dados
colour = (121, 125, 121)
lobby = True
running = True
# ===== Loop principal =====
while running:

    while lobby:
        image = pygame.image.load('Captura de tela 2024-10-30 184033.png')
        window.blit(image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # ----- Verifica consequências
            if event.type == pygame.KEYDOWN:
                    play = True
                    lobby = False
                    window.fill(colour)
                    pygame.display.update() 
                    break
    while play:

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
