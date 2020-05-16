import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    ''' Uma classe que representa um único alienígena da frota. '''

    def __init__(self, ai_settings, screen):
        ''' Inicializa o alienígina e define sua posição inicial. '''

        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem do alienígena e define seu atributo rect.
        self.image = pygame.image.load('images/nave-alien.png')
        self.rect = self.image.get_rect()

        # Inicia cada novo alienígena próximo à parte superior esquerdo da tela.
        self.rect.x = self.rect.width # Coloca um espaço à esquerda que seja igual à largura do alienígena.
        self.rect.y = self.rect.height # Coloca um espaço acima dele correspondente à sua altura.

        # Armazena a posição exata do alienígena.
        self.x = float(self.rect.x)

    def blitme(self):
        ''' Desenha o alienigina em sua posição atual. '''

        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        ''' Devolve True se o alienígena estiver na borda da tela. '''

        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        
        elif self.rect.left <= 0:
            return True


    def update(self):
        ''' Move o alienígena para a direita ou para a esquerda. '''

        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction) 
        ''' Permite o movimento para esquerda ou para a direita multiplicando o fator de velocidade
            do alienígena pelo valor de fleet_direction. '''
        self.rect.x = self.x # Atualiza a posição do rect do alienígena com o valor de self.x.
