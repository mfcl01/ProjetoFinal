import pygame
from pygame import mixer
pygame.init()
mixer.init()
clock = pygame.time.Clock()
# ----- Gera tela principal
pygame.display.set_caption('atravesse a rua!')
window = pygame.display.set_mode((1000, 595))
image = pygame.image.load('assets\Captura de tela 2024-10-30 184033.png')
window.blit(image, (0, 0))
pygame.mixer.music.load('musica lobby.mp3')
pygame.mixer.music.play(-1)
# ----- Inicia estruturas de dados
colour = (255, 0, 0)
lobby = True
game = True
#font = pygame.font.Font('freesansbold.ttf', 50)
#text = font.render('Atravesse a Rua!', True, (255,0,0) , (0,128,255))
#textRect = text.get_rect()
#textRect.center = (500, 250)
#window.fill((255,255,255))
#window.blit(text, textRect)
# ===== Loop principal =====
while game:

    while lobby:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lobby = False
                game = False
            # ----- Verifica consequências
            if event.type == pygame.KEYDOWN:
                    lobby = False
            # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador
        pygame.display.flip()
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
