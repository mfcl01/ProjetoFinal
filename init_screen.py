import pygame
from pygame import mixer
pygame.init()
mixer.init()
clock = pygame.time.Clock()
# ----- Gera tela principal
pygame.display.set_caption('Atravesse a Rua!')
window = pygame.display.set_mode((1000, 595))
image = pygame.image.load("assets folder/imagens/Captura de tela 2024-10-30 184033.png")
image = pygame.image.load('Captura de tela 2024-10-30 184033.png')
window.blit(image, (0, 0))
pygame.mixer.music.load('musica lobby.mp3')
pygame.mixer.music.play(-1)
pygame.display.update() 
# ----- Inicia estruturas de dados
colour = (255, 0, 0)
lobby = True
running = True
# ===== Loop principal =====
while running:

    while lobby:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # ----- Verifica consequências
            if event.type == pygame.KEYDOWN:
                    play = True
                    lobby = False
                    break
    window.fill(colour)
    pygame.display.update() 
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                running = False
            if event.type == pygame.KEYDOWN:
                play = False
                running = False
            
            
    
                    
            # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador
        pygame.display.flip()
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
