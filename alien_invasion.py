import sys
import pygame
from settings import Settings
from ship import Ship
from background import Background
import game_functions as gf 
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

''' O módulo sys é utilizado para sair do jogo quando o usuário desistir. '''

def run_game():

    # Inicializa o pygame, as configuraçoes e o objeto screen.
    pygame.init() # Inicia as configuraçôes de segundo plano.
    ai_settings = Settings() # Cria uma instância.
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # Superfície onde definimos sua dimensão. É uma janela de exibições para desenhar todos os elementos gráficos do jogo.
    
    pygame.display.set_caption("Alien Invasion - By Portela")

    # Cria o botão Play.
    play_button = Button(ai_settings, screen, "Play") # cria uma instância.

    # Cria instância para armazenar estatísticas do jogo e cria painel de pontuação.
    stats = GameStats(ai_settings) # cria uma instância.

    # Obtem a pontuação máxima.
    stats.high_score = gf.updateFile(stats)

    sb = Scoreboard(ai_settings, screen, stats) # cria uma instância.

    # Cria uma espaçonave.
    ship = Ship(ai_settings, screen)

    # Cria um grupo no qual serão armazenados os projéteis.
    bullets = Group() # cria uma instância.

    # Cria um grupo de alienígenas.
    aliens = Group() # cria uma instância.

    # Cria o Background.
    background = Background('images/earth.bmp', [0,0])

    # Cria a frota de alienígenas.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Inicia o laço principal do jogo.
    while True:

        # Observa eventos de teclado e de mouse.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ''' O jogo deverá ficar congelado quando todas as três espaçonaves forem usadas. '''

            # Atualiza a posição da espaçonave de acordo com a flag de movimento.
            ship.update()

            ''' Atualiza as posiçôes dos projéteis de acordo com a flag de movimento da espaçonave
                e livra-se dos projéteis que desapareceram. '''
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)

            # Monitora o número de espaçonaves que restam ao jogador.
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

        # Pega as posiçôes atualizadas e redesenha uma nova tela a cada passagem pelo laço.
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, background, bullets, play_button)
        
run_game()
