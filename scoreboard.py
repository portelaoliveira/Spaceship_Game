import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    ''' Uma classe para mostrar informações sobre pontuação. '''

    def __init__(self, ai_settings, screen, stats):
        ''' Inicializa os atributos da pontuação. '''

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Configurações de fonte para as inforemções de pontuação.
        self.text_color = (255, 0, 0) # Cor do texto.
        self.font = pygame.font.SysFont(None, 48) # Instanciamos para a fonte.

        # Prepara a imagem da pontuação inicial.
        self.prep_score()

        # Prepara a imagem da pontuação máxima.
        self.prep_high_score()

        # Prepara a imagem do nível do jogo.
        self.prep_level()

        # Cria um grupo de espaçonaves para indicar aos jogadores o número de espaçonaves restantes.
        self.prep_ships()

    def prep_ships(self):
        ''' Mostra quantas espaçonaves restam. '''

        self.ships = Group() # Cria um grupo vazio para armazenar instâncias das espaçonaves.
        for ship_number in range(self.stats.ships_left): # Percorre todas as espaçonaves que restam ao jogador.
            ship = Ship(self.ai_settings, self.screen) # Cria uma nova espaçonave.
            ship.rect.x = 10 + ship_number * ship.rect.width # Faz as espaçonaves aparecerem uma ao lado da outra, com uma margem de 10 pixels do lado esquerdo do grupo de espaçonaves.
            ship.rect.y = 10 # 10 pixels abaixo da parte superior da tela para que as espaçonaves estejam alinhadas com a imagem da pontuação.
            self.ships.add(ship) # Adiciona cada nova espaçonave ao grupo ships.

    def prep_level(self):
        ''' Transforma o nível em uma imagem renderizada. '''

        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color) # Cria a imagem.

        # Posiona o nível abaixo da pontuação.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right # Define o atributo right da imagem para que seja igual ao atributo right da pontuação.
        self.level_rect.top = self.score_rect.bottom + 10 
        ''' O atributo top é definido a 10 pixels abaixo da parte inferior da imagem da pontuação
            de modo a deixar um espaço entre a pontuação e o nível. '''

    def prep_high_score(self):
        ''' Transforma a pontuação máxima em uma imagem renderizada. '''

        high_score = int(round(self.stats.high_score, -1)) # Diz a python para arrendondar o valor de stats.score para o multíplo mais próximo de 10.
        high_score_str = "{:,}".format(high_score) # Tranforma o valor númerico em uma string e a formatamos com vírgulas para render.
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color) # Gera uma imagem com a pontuação máxima.

        # Centraliza a pontuação máxima na parte superior da tela.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top        

    def prep_score(self):
        ''' Transforma a pontuação em uma imagem renderizada. '''

        rounded_score = int(round(self.stats.score, -1)) # Diz a python para arrendondar o valor de stats.score para o multíplo mais próximo de 10.
        score_str = "{:,}".format(rounded_score) # Tranforma o valor númerico em uma string e a formatamos com vírgulas para render.
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color) # Transforma em uma imagem.

        # Exibe a pontuação na parte supetrior direito da tela.
        self.score_rect = self.score_image.get_rect() # Garante que a pontuação sempre seja alinhada com o lado direito.
        self.score_rect.right = self.screen_rect.right - 20 # Define a borda direita da pontuação a 20 pixels da borda direita da tela.
        self.score_rect.top = 20 # Posiciona a borda superior da pontuação 20 pixels abaixo da parte superior da tela.

    def show_score(self):
        ''' Exibe a imagem rendereizada da pontuação. '''

        self.screen.blit(self.score_image, self.score_rect) 
        ''' Esse método desenha a imagem da pontuação na tela no local especificado por score_rect. '''

        self.screen.blit(self.high_score_image, self.high_score_rect)
        ''' Desenha a pontuação máxima na parte superior central da tela. '''

        self.screen.blit(self.level_image, self.level_rect)
        ''' Adiciona uma linha para desenhar a imagem do nível do jogo na tela. '''
        
        self.ships.draw(self.screen)
        ''' Desenha as espaçonaves que restam ao jogador. '''
