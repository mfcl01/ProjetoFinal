import pygame
from pygame import mixer
pygame.init()
mixer.init()
clock = pygame.time.Clock()
# ----- Gera tela principal
pygame.display.set_caption('Atravesse a Rua!')
window = pygame.display.set_mode((1000, 595))
<<<<<<<< HEAD:lobby.py
image = pygame.image.load('assets\imagens\Captura de tela 2024-10-30 184033.png')
========
image = pygame.image.load('Captura de tela 2024-10-30 184033.png')
>>>>>>>> c579bcb993384a6c5ce41aceb3450d05ff18cdc1:Atravesse_a_rua.py
window.blit(image, (0, 0))
pygame.mixer.music.load('musica lobby.mp3')
pygame.mixer.music.play(-1)
# ----- Inicia estruturas de dados
colour = (255, 0, 0)
lobby = True
game = True
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
