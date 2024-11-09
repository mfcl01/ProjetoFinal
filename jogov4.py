import pygame
import sys
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
pygame.mixer.music.load('musica lobby.mp3')
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

# Condições Iniciais
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

# PARTE PARA REVISAR ANTES DE DAR COMMIT
# mexer no + 200 para ver altura do retangulo

# Botao Play

rect_largura, rect_altura = 200, 100
# //Atras do botão
rect_largura_fundo, rect_altura_fundo = 220, 120 
rect_largura_fundo_titulo, rect_altura_fundo_titulo = 500, 65 
rect_x_play = (largura - rect_largura) // 2
rect_y_play = ((altura - rect_altura) // 2) + 200
# Botao Quit
rect_x_quit = (largura - rect_largura) // 2
rect_y_quit = ((altura - rect_altura) // 2) + 350
rect_quit = pygame.Rect(rect_x_quit, rect_y_quit, rect_largura, rect_altura)

rect_play = pygame.Rect(rect_x_play, rect_y_play, rect_largura, rect_altura)
rect_play_fundo = pygame.Rect(rect_x_play-10, rect_y_play-10, rect_largura_fundo, rect_altura_fundo)
rect_play_fundo_2 = pygame.Rect(rect_x_play-10, rect_y_play+140, rect_largura_fundo, rect_altura_fundo)
rect_fundo_titulo = pygame.Rect(rect_x_quit-133,rect_y_quit-495, rect_largura_fundo_titulo, rect_altura_fundo_titulo)



fonte_texto = pygame.font.Font("assets folder/pixelatedczs.ttf", 48)
texto_button_play = fonte_texto.render('PLAY', True, (255, 255, 255))  
texto_button_quit = fonte_texto.render('QUIT', True, (255, 255, 255)) 
text_rect_play = texto_button_play.get_rect(center=rect_play.center)
text_rect_quit = texto_button_play.get_rect(center=rect_quit.center)


font_pixel = pygame.font.Font("assets folder/pixelatedczs.ttf",52)
titulo_jogo = font_pixel.render("ATRAVESSE A RUA",True,(247, 105, 2))
titulo_jogo_2 = font_pixel.render("ATRAVESSE A RUA",True,(200, 0, 0))
# window.blit(titulo_jogo,(rect_x_quit-116,rect_y_quit-500))
# window.blit(titulo_jogo_2,(rect_x_quit-121,rect_y_quit-500))

# pygame.display.flip()
# pygame.display.update()
image_lobby = pygame.image.load('BACKGROUND J4.png')
image_lobby = pygame.transform.scale(image_lobby, (largura, altura))

window.blit(image_lobby, (0, 0))
pygame.draw.rect(window, (255, 255, 255), rect_fundo_titulo)
pygame.draw.rect(window, (247, 105, 2), rect_play)
pygame.draw.rect(window, (255, 255, 255), rect_play_fundo)
pygame.draw.rect(window, (255, 255, 255), rect_play_fundo_2)
pygame.draw.rect(window, (247, 105, 2), rect_quit)

# ===== Loop principal =====
while running:

    if tela == 'lobby':
        window.blit(titulo_jogo_2,(rect_x_quit-121,rect_y_quit-500))
        window.blit(titulo_jogo,(rect_x_quit-116,rect_y_quit-500))
        pygame.display.flip()
        pygame.display.update()
        pontos = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if rect_play.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(window,(209, 204, 201), rect_play_fundo)
                pygame.draw.rect(window, (200, 0, 0), rect_play)
                texto_button_play = fonte_texto.render('PLAY', True, (209, 204, 201)) 
                window.blit(texto_button_play, text_rect_play)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    tela = "play"
            if not rect_play.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(window, (255, 255, 255), rect_play_fundo)
                pygame.draw.rect(window, (247, 105, 2), rect_play)
                texto_button_play = fonte_texto.render('PLAY', True, (255, 255, 255)) 
                window.blit(texto_button_play, text_rect_play)

                # ABAIXO é o quit
            if rect_quit.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(window,(209, 204, 201), rect_play_fundo_2)
                pygame.draw.rect(window, (200, 0, 0), rect_quit)
                texto_button_quit = fonte_texto.render('QUIT', True, (209, 204, 201)) 
                window.blit(texto_button_quit, text_rect_quit)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    running = False
            if not rect_quit.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(window,(255, 255, 255), rect_play_fundo_2)
                pygame.draw.rect(window, (247, 105, 2), rect_quit)
                texto_button_quit = fonte_texto.render('QUIT', True, (255, 255, 255)) 
                window.blit(texto_button_quit, text_rect_quit)
                


    if tela == 'play':
        texto_score = fonte_texto.render("SCORE: "+str(pontos), True, (255,255,255))
        window.blit(texto_score,[15,15])
        font = pygame.font.SysFont(None, 48)
        keys = pygame.key.get_pressed()

        for sprite in all_sprites:
            sprite.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Sair do jogo
        if keys[pygame.K_ESCAPE]:
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
            pontos += 1
            # for veiculo in veiculos_sprites:
            #     veiculo.aumenta_velocidade()
            # rua_sprite.image = fazenda
            # rua2_sprite.image = fazenda


        if rua2_sprite.rect.y >= altura:
            rua2_sprite.rect.y = -altura
        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

        window.fill((0, 0, 0))  # Limpa a tela para não deixar rastros
        all_sprites.draw(window)
        players.draw(window)
        texto_score = fonte_texto.render("SCORE: "+str(pontos), True, (255,255,255))
        window.blit(texto_score,[15,15])
    
    pygame.display.flip()
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados