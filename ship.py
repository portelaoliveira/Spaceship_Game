import pygame
from pygame.sprite import Sprite
''' A classe Ship herda Sprite parra que seja possível cria um grupo de espaçonaves para indicar 
    o número de espaçonaves restantes ao jogadores. '''

class Ship(Sprite):

    def __init__(self, ai_settings, screen): # O parâmetro screen é a tela que desenha a espaçonave.
        ''' Inicializa a espaçonave e define sua posição inicial. '''

        super(Ship, self).__init__()
        
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem da espaçonave e obtém seu rect.
        self.image = pygame.image.load('images/nave-2.png') # A função carrega a imagem e devolve uma uperfície que representa a espaçonave.
        self.rect = self.image.get_rect() # Acessa o tributo rect da superfície. O Pygame trata os elementos do jogo como retângulos.
        self.screen_rect = screen.get_rect() # Posicionar a espaçonave na parte inferior central da tela. Armazenar o retângulo da tela.

        # Inicia cada nova spaçonave na parte inferior central da tela.
        self.rect.centerx = self.screen_rect.centerx # A cooredenada x do centro da espaçonave e faz concidir com a atributo centerx do retângulo da tela.
        self.rect.bottom = self.screen_rect.bottom # A cooredenada y do centro da espaçonave e faz concidir com a atributo centerx do retângulo da tela.

        # Armazena um velor decimal para o centro da espaçonave.
        self.center = float(self.rect.centerx)
        
        # Flag de movimento.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        ''' Atualiza a posição da espaçonave de acordo com a flag de movimento. '''
        # Atualiza o valor do  centro da espaçonave, e não o retângulo.
        if self.moving_right and self.rect.right < self.screen_rect.right: # Se o flag for True, move para a direita.
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0: # Se o flag for True, move para a esquerda.
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.top > 250: # Se o flag for True, move para cima (*).
            self.rect.top -= self.ai_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom: # Se o flag for True, move para baixo.
            self.rect.bottom += self.ai_settings.ship_speed_factor

        # Atualiza o objeto rect de acordo com self.center.
        self.rect.centerx = self.center
        
    def blitme(self):
        ''' Desenha a espaçonave em sua posição atual. '''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        ''' Centraliza a espaçonave na tela. '''

        self.center = self.screen_rect.centerx
