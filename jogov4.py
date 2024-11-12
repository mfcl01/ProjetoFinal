import pygame
import sys
from pygame import mixer
import assets
import config
from sprites import *
import sprite_ajuda

pygame.init()
mixer.init()
clock = pygame.time.Clock()
# ----- Gera tela principal
pygame.display.set_caption('Atravesse a Rua!')
largura, altura = pygame.display.Info().current_w, pygame.display.Info().current_h
window = pygame.display.set_mode((largura, altura), pygame.FULLSCREEN)
# largura, altura = 1200,800
# window = pygame.display.set_mode((1200, 800))


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

# raposa_img = pygame.image.load('raposa.webp')
raposa_img = pygame.image.load('raposa.webp')
raposa = pygame.transform.scale(raposa_img,(assets.LARGURA_RAPOSA, assets.ALTURA_RAPOSA))




carro_img = pygame.image.load('Carro azul.png').convert_alpha()
carro = pygame.transform.scale(carro_img, (assets.LARGURA_DO_CARRO, assets.ALTURA_DO_CARRO))
rect_carro = carro_img.get_rect()

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

# FUNDO DOS PERSONAGENS
rect_personagem_fundo = pygame.Rect(300, 450, rect_largura_fundo-120, rect_altura_fundo-10)
rect_personagem_fundo_2 = pygame.Rect(500, 450, rect_largura_fundo-120, rect_altura_fundo-10)
rect_personagem_fundo_3 = pygame.Rect(700, 450, rect_largura_fundo-120, rect_altura_fundo-10)
rect_personagem_fundo_4 = pygame.Rect(900, 450, rect_largura_fundo-120, rect_altura_fundo-10)
rect_personagem_fundo_5 = pygame.Rect(1100, 450, rect_largura_fundo-120, rect_altura_fundo-10)

rect_play_fundo_2 = pygame.Rect(rect_x_play-10, rect_y_play+140, rect_largura_fundo, rect_altura_fundo)
rect_fundo_titulo = pygame.Rect(rect_x_quit-133,rect_y_quit-495, rect_largura_fundo_titulo, rect_altura_fundo_titulo)
# rect_fundo_personagem = pygame.Rect(rect_x_quit-150,rect_y_quit-495, rect_largura_fundo_titulo, rect_altura_fundo_titulo)




fonte_texto = pygame.font.Font("assets folder/pixelatedczs.ttf", 48)
fonte_texto_menor = pygame.font.Font("assets folder/pixelatedczs.ttf", 40)
fonte_texto_maior = pygame.font.Font("assets folder/pixelatedczs.ttf", 100)
texto_button_play = fonte_texto.render('PLAY', True, (255, 255, 255))
texto_button_restart = fonte_texto_menor.render('RESTART', True, (255, 255, 255))  
texto_button_quit = fonte_texto.render('QUIT', True, (255, 255, 255)) 
text_rect_play = texto_button_play.get_rect(center=rect_play.center)

text_rect_restart = texto_button_restart.get_rect(center=(rect_play.centerx + 5 , rect_play.centery))

text_rect_quit = texto_button_play.get_rect(center=rect_quit.center)



font_pixel = pygame.font.Font("assets folder/pixelatedczs.ttf",52)
titulo_jogo = font_pixel.render("ATRAVESSE A RUA",True,(247, 105, 2))
titulo_jogo_2 = font_pixel.render("ATRAVESSE A RUA",True,(200, 0, 0))
titulo_personagens = font_pixel.render("ESCOLHE SEU PERSONAGEM",True,(255, 255, 255 ))


# ========================================================================================================================

# SPRITE COM ANIMAÇÃO VARIAVEIS ABAIXO 
fox = "FOXSPRITESHEET.png"
imagem_raposa_escolher = pygame.image.load("frame_17_fox.png")
imagem_scale_raposa = pygame.transform.scale(imagem_raposa_escolher,(92,92))

raccoon = "RACCOONSPRITESHEET.png"
imagem_raccoon_escolher = pygame.image.load("frame_17_raccoon.png")
imagem_scale_raccoon = pygame.transform.scale(imagem_raccoon_escolher,(92,92))

bird = "BIRDSPRITESHEET.png"
imagem_bird_escolher = pygame.image.load("frame_17_bird.png")
imagem_scale_bird = pygame.transform.scale(imagem_bird_escolher,(92,92))

cat_gray = "CATGRAYSPRITESHEET.png"
imagem_catgray_escolher = pygame.image.load("frame_17_catgray.png")
imagem_scale_catgray = pygame.transform.scale(imagem_catgray_escolher,(92,92))

cat_orange = "CATORANGESPRITESHEET.png"
imagem_catorange_escolher = pygame.image.load("frame_17_catorange.png")
imagem_scale_catorange = pygame.transform.scale(imagem_catorange_escolher,(92,92))


# USAR A SEGUINTE VARIAVEL PARA ESCOLHER PERSONAGEM
personagem = raccoon
current_character = str(personagem)

sprite_character_image = pygame.image.load(personagem).convert_alpha()
sprite_character_image_rc = pygame.image.load(personagem).convert_alpha()

sprite_sheet = sprite_ajuda.SpriteSheet(sprite_character_image)
sprite_sheet = sprite_ajuda.SpriteSheet(sprite_character_image_rc)

personagem_atual = {fox:"frame_17_fox.png",raccoon:"frame_17_raccoon.png",bird:"frame_17_bird.png",cat_gray:"frame_17_catgray.png",cat_orange:"frame_17_catorange.png"}
morreu_img = pygame.image.load(personagem_atual[personagem]).convert_alpha()

def pegar_imagem(sheet, frame, width, height, scale):
    image = pygame.Surface((width,height), pygame.SRCALPHA).convert_alpha()
    image.blit(sheet,(0, 0), ((frame *  width), 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    return image 


# Acoes
idle_frontal = 0
idle_direita = 1
idle_esquerda = 2
idle_atras = 3
frontal = 4
direita = 5
esquerda = 6
atras = 7
correr_abaixo = 8
correr_esquerda = 9 
correr_direita = 10 
correr_cima = 11

# Lista de animação
lista_animacao = []
animacao_passos = [4,4,4,4,1,1,1,1,8,8,8,8]
last_update = pygame.time.get_ticks()


animacao_tempo_espera = 100
frame = 0
contador_passo = 0




for animacao in animacao_passos:
    img_temp_lista = []
    for _ in range(animacao):
        img_temp_lista.append(sprite_sheet.pegar_imagem(contador_passo,32,32,3))
        contador_passo += 1
    lista_animacao.append(img_temp_lista)


# raposa retangulo
orientacao_atual = "down"
acao = idle_frontal
# sprite_rect = lista_animacao[acao][0].get_rect()
sprite_rect_x = 1536 / 2 - 100
sprite_rect_y = 680

tombstone_img_og = pygame.image.load("Tombstone.png").convert_alpha()
tombstone_img = pygame.transform.scale(tombstone_img_og,(250,250))
rect_tombstone = tombstone_img.get_rect()
centro_tela = window.get_rect().center
centro_mudado = (centro_tela[0] - 5, centro_tela[1])
rect_tombstone.center = centro_mudado



image_lobby = pygame.image.load('BACKGROUND J4.png')
image_lobby = pygame.transform.scale(image_lobby, (largura, altura))
window.blit(image_lobby, (0, 0))
pygame.draw.rect(window, (255, 255, 255), rect_fundo_titulo)
pygame.draw.rect(window, (247, 105, 2), rect_play)
pygame.draw.rect(window, (255, 255, 255), rect_play_fundo)
pygame.draw.rect(window, (255, 255, 255), rect_play_fundo_2)
pygame.draw.rect(window, (247, 105, 2), rect_quit)

ultimos_pontos = 0


img_frame_atual = lista_animacao[acao][frame]
frame_atual_mask = pygame.mask.from_surface(img_frame_atual)
sprite_rect = img_frame_atual.get_rect(topleft=(sprite_rect_x,sprite_rect_y))

# =========================================================================================================
# ===== Loop principal =====
while running:
    tempo_agora = pygame.time.get_ticks()
    mouse_pos = pygame.mouse.get_pos()
    hover_play = rect_play.collidepoint(mouse_pos)
    hover_quit = rect_quit.collidepoint(mouse_pos)

    
    if tela == 'lobby':
        window.blit(titulo_jogo_2,(rect_x_quit-121,rect_y_quit-500))
        window.blit(titulo_jogo,(rect_x_quit-116,rect_y_quit-500))
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
                    tela = "character" # Testando tela nova mudar para "play depois"

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
                

    if tela == "character":
        pygame.display.set_caption('Escolha o personagem')
        window.fill((27, 130, 7))
        keys = pygame.key.get_pressed()
        tempo_agora = pygame.time.get_ticks()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if rect_personagem_fundo.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                    personagem = raccoon
                    running = False
                    sprite_rect_x = 1536 / 2 - 100
                    sprite_rect_y = 680
                    sprite_character_image = pygame.image.load(personagem).convert_alpha()
                    sprite_sheet = sprite_ajuda.SpriteSheet(sprite_character_image)
                    lista_animacao = []
                    animacao_passos = [4,4,4,4,1,1,1,1,8,8,8,8]
                    last_update = pygame.time.get_ticks()
                    animacao_tempo_espera = 100
                    frame = 0
                    contador_passo = 0
                    morreu_img_og = pygame.image.load(personagem_atual[personagem]).convert_alpha()
                

                    for animacao in animacao_passos:
                        img_temp_lista = []
                        for _ in range(animacao):
                            img_temp_lista.append(sprite_sheet.pegar_imagem(contador_passo,32,32,3))
                            contador_passo += 1
                        lista_animacao.append(img_temp_lista)
                    running = True 
                    tela = "play" # Testando tela nova mudar para "play depois"
        if rect_personagem_fundo_2.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                    personagem = bird
                    running = False
                    sprite_rect_x = 1536 / 2 - 100
                    sprite_rect_y = 680
                    sprite_character_image = pygame.image.load(personagem).convert_alpha()
                    sprite_sheet = sprite_ajuda.SpriteSheet(sprite_character_image)
                    lista_animacao = []
                    animacao_passos = [4,4,4,4,1,1,1,1,8,8,8,8]
                    last_update = pygame.time.get_ticks()
                    animacao_tempo_espera = 100
                    frame = 0
                    contador_passo = 0
                    morreu_img_og = pygame.image.load(personagem_atual[personagem]).convert_alpha()
                    for animacao in animacao_passos:
                        img_temp_lista = []
                        for _ in range(animacao):
                            img_temp_lista.append(sprite_sheet.pegar_imagem(contador_passo,32,32,3))
                            contador_passo += 1
                        lista_animacao.append(img_temp_lista)
                    running = True 
                    tela = "play" # Testando tela nova mudar para "play depois"
        if rect_personagem_fundo_3.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                    personagem = fox
                    running = False
                    sprite_rect_x = 1536 / 2 - 100
                    sprite_rect_y = 680
                    sprite_character_image = pygame.image.load(personagem).convert_alpha()
                    sprite_sheet = sprite_ajuda.SpriteSheet(sprite_character_image)
                    lista_animacao = []
                    animacao_passos = [4,4,4,4,1,1,1,1,8,8,8,8]
                    last_update = pygame.time.get_ticks()
                    animacao_tempo_espera = 100
                    frame = 0
                    contador_passo = 0
                    morreu_img_og = pygame.image.load(personagem_atual[personagem]).convert_alpha()

                    for animacao in animacao_passos:
                        img_temp_lista = []
                        for _ in range(animacao):
                            img_temp_lista.append(sprite_sheet.pegar_imagem(contador_passo,32,32,3))
                            contador_passo += 1
                        lista_animacao.append(img_temp_lista)
                    running = True  
                    tela = "play" # Testando tela nova mudar para "play depois"

        if rect_personagem_fundo_4.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                    personagem = cat_orange
                    running = False
                    sprite_rect_x = 1536 / 2 - 100
                    sprite_rect_y = 680
                    sprite_character_image = pygame.image.load(personagem).convert_alpha()
                    sprite_sheet = sprite_ajuda.SpriteSheet(sprite_character_image)
                    lista_animacao = []
                    animacao_passos = [4,4,4,4,1,1,1,1,8,8,8,8]
                    last_update = pygame.time.get_ticks()
                    animacao_tempo_espera = 100
                    frame = 0
                    contador_passo = 0
                    morreu_img_og = pygame.image.load(personagem_atual[personagem]).convert_alpha()

                    for animacao in animacao_passos:
                        img_temp_lista = []
                        for _ in range(animacao):
                            img_temp_lista.append(sprite_sheet.pegar_imagem(contador_passo,32,32,3))
                            contador_passo += 1
                        lista_animacao.append(img_temp_lista)
                    running = True 
                    tela = "play" # Testando tela nova mudar para "play depois"              
        if rect_personagem_fundo_5.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                    personagem = cat_gray
                    running = False
                    sprite_rect_x = 1536 / 2 - 100
                    sprite_rect_y = 680
                    sprite_character_image = pygame.image.load(personagem).convert_alpha()
                    sprite_sheet = sprite_ajuda.SpriteSheet(sprite_character_image)
                    lista_animacao = []
                    animacao_passos = [4,4,4,4,1,1,1,1,8,8,8,8]
                    last_update = pygame.time.get_ticks()
                    animacao_tempo_espera = 100
                    frame = 0
                    contador_passo = 0
                    morreu_img_og = pygame.image.load(personagem_atual[personagem]).convert_alpha()

                    for animacao in animacao_passos:
                        img_temp_lista = []
                        for _ in range(animacao):
                            img_temp_lista.append(sprite_sheet.pegar_imagem(contador_passo,32,32,3))
                            contador_passo += 1
                        lista_animacao.append(img_temp_lista)
                    running = True 
                    tela = "play" # Testando tela nova mudar para "play depois"              
                        

            

        if tempo_agora - last_update >= animacao_tempo_espera:
            frame += 1
            last_update = tempo_agora
            if frame >= len(lista_animacao[acao]):
                frame = 0
                
        # Sair do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if keys[pygame.K_ESCAPE]:
                running = False


        window.blit(titulo_personagens,(rect_x_quit-250,rect_y_quit-500))
        pygame.draw.rect(window,(92, 91, 87), rect_personagem_fundo)
        window.blit(imagem_scale_raccoon,(302.5,455))

        
        pygame.draw.rect(window,(35, 179, 232), rect_personagem_fundo_2)
        window.blit(imagem_scale_bird,(502.5,455))

        pygame.draw.rect(window,(191, 128, 44), rect_personagem_fundo_3)
        window.blit(imagem_scale_raposa,(702.5,455))
        
        pygame.draw.rect(window,(247, 141, 0), rect_personagem_fundo_4)
        window.blit(imagem_scale_catorange,(902.5,455))

        pygame.draw.rect(window,(130, 128, 126), rect_personagem_fundo_5)
        window.blit(imagem_scale_catgray,(1102.5,455))


    if tela == 'play':
            texto_score = fonte_texto.render("SCORE: "+str(pontos), True, (255,255,255))
            window.blit(texto_score,[15,15])
            font = pygame.font.SysFont(None, 48)
            keys = pygame.key.get_pressed()

            if tempo_agora - last_update >= animacao_tempo_espera:
                frame += 1
                last_update = tempo_agora
                if frame >= len(lista_animacao[acao]):
                    frame = 0

            for sprite in all_sprites:
                sprite.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Sair do jogo
            if keys[pygame.K_ESCAPE]:
                    running = False
            # MOVIMENTAÇÃO DA SPRITE COM ANIMAÇÃO
            if keys[pygame.K_UP]:
                orientacao_atual = "up"
                sprite_rect_y -= velocidade + 10
                sprite_rect.topleft = (sprite_rect_x, sprite_rect_y)
                acao = correr_cima

                for sprite in all_sprites:
                    sprite.rect.y += velocidade
                y += velocidade
                y2 += velocidade

            elif keys[pygame.K_DOWN]:
                orientacao_atual = "down"
                sprite_rect_y += velocidade + 10
                sprite_rect.topleft = (sprite_rect_x, sprite_rect_y)
                acao = correr_abaixo
                


                for sprite in all_sprites:
                    sprite.rect.y -= velocidade
            
                y -= velocidade
                y2 -= velocidade 
            elif keys[pygame.K_RIGHT]:
                orientacao_atual = "right"
                sprite_rect_x += velocidade + 10
                sprite_rect.topleft = (sprite_rect_x, sprite_rect_y)
                acao = correr_direita

                for player in players:
                    player.rect.x += velocidade 
            elif keys[pygame.K_LEFT]:
                orientacao_atual = "left"
                sprite_rect_x -= velocidade + 10
                sprite_rect.topleft = (sprite_rect_x, sprite_rect_y)
                acao = correr_esquerda
                for player in players:
                    player.rect.x -= velocidade
            elif keys[pygame.K_c]:
                tela = "character"
            else:
                if orientacao_atual == "down":
                    if acao != idle_frontal:
                        acao = idle_frontal
                        frame = 0
                if orientacao_atual == "up":
                    if acao != idle_atras:
                        acao = idle_atras
                        frame = 0
                if orientacao_atual == "left":
                    if acao != idle_esquerda:
                        acao = idle_esquerda
                        frame = 0
                if orientacao_atual == "right":
                    if acao != idle_direita:
                        acao = idle_direita
                        frame = 0


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
            
            
            for veiculo in veiculos_sprites:
                desvio = (veiculo.rect.x - sprite_rect_x,veiculo.rect.y-sprite_rect_y)
                if frame_atual_mask.overlap(veiculo.mask, desvio):
                    window.fill((194, 12, 2))
                    pygame.display.update()
                    ultimos_pontos = pontos
                    pygame.time.delay(100)
                    tela = 'morte'
                    break



            if rua2_sprite.rect.y >= altura:
                rua2_sprite.rect.y = -altura
            # ----- Atualiza estado do jogo
            pygame.display.update()  # Mostra o novo frame para o jogador

            window.fill((0, 0, 0))  # Limpa a tela para não deixar rastros
            all_sprites.draw(window)
            players.draw(window)
            window.blit(lista_animacao[acao][frame],(sprite_rect_x,sprite_rect_y ))

            texto_score = fonte_texto.render("SCORE: "+str(pontos), True, (255,255,255))
            window.blit(texto_score,(15,15))
        
    if tela == 'morte':
        keys = pygame.key.get_pressed()
        # window.fill((194, 12, 2))   Possible leave red or not ask to see what is better
        # Criação de uma cor que seja transparente com uma opacidade menor para conseguir ver onde perdeu o jogo 
        transparente_cor = pygame.Surface((window.get_width(), window.get_height()), pygame.SRCALPHA)
        transparente_cor.fill((194, 0, 0, 1.275))
        window.blit(transparente_cor, (0, 0))

        window.blit(tombstone_img,rect_tombstone)
        morreu_img = pygame.transform.scale(morreu_img_og,(188,188))
        texto_score_ultimo = fonte_texto.render("SCORE: "+str(ultimos_pontos), True, (255,255,255))
        window.blit(morreu_img, (rect_tombstone.x+40,rect_tombstone.y+10)) 
        window.blit(texto_score,(rect_x_quit-5,rect_y_quit-500))
        game_over = fonte_texto_maior.render("GAME OVER", True, (255,255,255))
        window.blit(game_over,(rect_x_quit-165,rect_y_quit-650))
        # MUDAR PERSONAGEM BOTÃO
        # Add tombstone and in the middle the picture of the character used
        # Add the score which the player achieved in that game 

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if keys[pygame.K_c]:
            tela = "character"
        if rect_play.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window,(209, 204, 201), rect_play_fundo)
            pygame.draw.rect(window, (27, 130, 7), rect_play)
            texto_button_restart = fonte_texto_menor.render('RESTART', True, (209, 204, 201))
            window.blit(texto_button_restart, text_rect_restart) 
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False

                for sprite in all_sprites:
                    sprite.reset_y()
                    sprite.reset_x()
                

                acao = idle_frontal
                orientacao_atual = "down"
                
                sprite_rect_x = 1536 / 2  - 100
                sprite_rect_y = 680
                pontos = 0
                frame = 0

                if tempo_agora - last_update >= animacao_tempo_espera:
                    frame += 1
                    last_update = tempo_agora
                    if frame >= len(lista_animacao[acao]):
                        frame = 0

                 
                tela = "play"
                running = True

                

        if not rect_play.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window, (255, 255, 255), rect_play_fundo)
            pygame.draw.rect(window, (247, 105, 2), rect_play)
            texto_button_restart = fonte_texto_menor.render('RESTART', True, (255, 255, 255)) 
            window.blit(texto_button_restart, text_rect_restart)

            
        if rect_quit.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window,(209, 204, 201), rect_play_fundo_2)
            pygame.draw.rect(window, (0, 0, 0), rect_quit)
            texto_button_quit = fonte_texto.render('QUIT', True, (209, 204, 201)) 
            window.blit(texto_button_quit, text_rect_quit)
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False

        if not rect_quit.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window,(255, 255, 255), rect_play_fundo_2)
            pygame.draw.rect(window, (247, 105, 2), rect_quit)
            texto_button_quit = fonte_texto.render('QUIT', True, (255, 255, 255)) 
            window.blit(texto_button_quit, text_rect_quit)
    pygame.display.flip()
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
