# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from pygame import mixer
pygame.init()
mixer.init()
clock = pygame.time.Clock()

# ----- Gera tela principal
window = pygame.display.set_mode((554, 554))
pygame.display.set_caption('Jogo do FEIN')
image = pygame.image.load(r'C:\Users\unesr\OneDrive\Área de Trabalho\DeSoft\Pygame\Travis.jpg')
window.blit(image, (0, 0))
#pygame.mixer.music.load(r'C:\Users\unesr\AppData\Local\Temp\fd52fc4e-efe4-4f32-b442-359463356a6a_fein travis.zip.a6a\Travis-Scott-FE-N-(RavenPop.com).mp3')
#pygame.mixer.music.play(-1)
x = 60
y = 60
color = (255, 0, 0)

# ----- Inicia estruturas de dados
game = True
fein = False
is_red = True
font = pygame.font.Font('freesansbold.ttf', 50)
text = font.render('GAME OVER', True, (255,0,0) , (0,128,255))
textRect = text.get_rect()
textRect.center = (250, 250)
window.fill((255,255,255))
window.blit(text, textRect)
# ===== Loop principal =====
while game:
    while not fein:
    # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_red = not is_red
            if is_red: color = (255, 0, 0)
            else: color = (102, 0, 0)
            

        

    # ----- Gera saídas
    #window.fill((0, 0, 0))  # Preenche com a cor azul
    #pygame.draw.rect(window, (255, 0, 0), pygame.Rect(x, y, 90, 90))

        pressed = pygame.key.get_pressed()
        if x<=0:
            x = 0
        elif x > 540:
            x = 540
        if y <=0:
            y= 0
        elif y > 540:
            y = 540
        window.blit(image, (0, 0))
        if pressed[pygame.K_UP]: y -= 1
        if pressed[pygame.K_DOWN]: y += 1
        if pressed[pygame.K_LEFT]: x -= 1
        if pressed[pygame.K_RIGHT]: x += 1
        clock.tick(3000)
        pygame.draw.rect(window, color, pygame.Rect(x, y, 90, 90))
        pygame.draw.circle(window, (255,255,0), (300,300),50, 10)
        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador
        pygame.display.flip()
        is_red = True


# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados