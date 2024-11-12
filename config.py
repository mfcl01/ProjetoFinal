from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG = path.join(path.dirname(__file__), 'assets', 'imagens')
SND = path.join(path.dirname(__file__), 'assets', 'sons')
FNT = path.join(path.dirname(__file__), 'assets', 'fontes')



# Dados gerais do jogo.
LARGURA = 1000 
ALTURA = 595 
FPS = 60

# Define tamanhos
LARGURA_DO_CARRO = 200
ALTURA_DO_CARRO = 250
LARGURA_CAMINHAO = 400
ALTURA_CAMINHAO = 400
LARGURA_RAPOSA = 32
ALTURA_RAPOSA = 32

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2