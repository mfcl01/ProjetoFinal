import pygame
from pygame import mixer
import assets
import config
from sprites import *

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
pygame.mixer.music.load('assets\sons\musica lobby.mp3')
pygame.mixer.music.play(-1)
pygame.display.update() 

# ----- Inicia estruturas de dados
players = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
veiculos_sprites = pygame.sprite.Group()
x, y = 0, 0
y2 = altura
rua = pygame.image.load('rua.jpeg')
rua = pygame.transform.scale(rua, (largura, altura))
# fazenda = pygame.image.load('fazenda.jpeg')
# fazenda = pygame.transform.scale(fazenda, (largura, altura))
rua_sprite = Background(rua, 0, 0)
all_sprites.add(rua_sprite)
rua2_sprite = Background(rua, 0, -altura)
all_sprites.add(rua2_sprite)
lobby = True
running = True
tela ='lobby'
raposa_img = pygame.image.load('raposa.webp')
raposa = pygame.transform.scale(raposa_img,(assets.LARGURA_RAPOSA, assets.ALTURA_RAPOSA))
carro_img = pygame.image.load('Carro azul.png').convert_alpha()
carro = pygame.transform.scale(carro_img, (assets.LARGURA_DO_CARRO, assets.ALTURA_DO_CARRO))
caminhao_img =pygame.image.load('caminhão_branco-removebg-preview.png').convert_alpha()
caminhao = pygame.transform.scale(caminhao_img, (config.LARGURA_CAMINHAO, config.ALTURA_CAMINHAO))
caminhao_sprite = Carro(caminhao, 1400, 80, -2.5)
all_sprites.add(caminhao_sprite)
veiculos_sprites.add(caminhao_sprite)
carro_sprite = Carro(carro, -150, 400, 2.5)
all_sprites.add(carro_sprite)
veiculos_sprites.add(carro_sprite)
raposa_sprite = Raposa(raposa)
players.add(raposa_sprite)
# carro_x = -150
# carro_y = 400
# carro_speed = 2.5
# caminhao_x = 1400
# caminhao_y = 80
velocidade = 2   # Quantos pixels o personagem se move por frame

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
        
        keys = pygame.key.get_pressed()

        for sprite in all_sprites:
            sprite.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if keys[pygame.K_UP]:
            for sprite in all_sprites:
                sprite.rect.y += velocidade
            y += velocidade
            y2 += velocidade

        if keys[pygame.K_DOWN]:
            for sprite in all_sprites:
                sprite.rect.y -= velocidade
        
            y -= velocidade
            y2 -= velocidade 
        if keys[pygame.K_RIGHT]:
            for player in players:
                player.rect.x += velocidade 
        if keys[pygame.K_LEFT]:
            for player in players:
                player.rect.x -= velocidade

        if y < 0:
            y = 0
            for sprite in all_sprites:
                sprite.reset_y()

        if y >= altura:
            y = -altura
            for sprite in all_sprites:
                sprite.reset_y()
                sprite.reset_x()
            for veiculo in veiculos_sprites:
                veiculo.aumenta_velocidade()
            for player in players:
                player.aumenta_velocidade()
          
            # rua_sprite.image = fazenda
            # rua2_sprite.image = fazenda




        if rua2_sprite.rect.y >= altura:
            rua2_sprite.rect.y = -altura


        # ----- Atualiza estado do jogo
        window.fill((0, 0, 0))  # Limpa a tela para não deixar rastros
        all_sprites.draw(window)
        players.draw(window)
        pygame.display.update()  # Mostra o novo frame para o jogador
        pygame.display.flip()
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados