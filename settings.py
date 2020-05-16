class Settings():
    ''' Uma classe para armazenar todas as configurações da Invação Alienígena. '''

    def __init__(self):
        ''' Inicializa as configurações estátisticas do jogo. '''

        # Configurações da tela.
        self.screen_width = 900 # Largura.
        self.screen_height = 504 # Altura.
        self.bg_color = (15, 15, 67) # Cor de fundo.

        # Configurações da espaçonave.
        self.ship_limit = 3 # Número de espaçonave com que o jogador começa.
        
        # Configurações dos projéteis da espaçonave.
        self.bullet_width = 3 # Largura dos projéteis.
        self.bullet_height = 6 # Altura dos projéteis.
        self.bullet_color = 255, 0, 0 # Cor dos prójeteis.
        self.bullets_allowed = 3 # Limita o jogador a três projéteis ao mesmo tempo.

        # Configurações dos alienígenas.
        self.fleet_drop_speed = 10 # Controla a velocidade com que a frota desce na tela sempre que um alienígena alcançar umas das bosdas.

        # A taxa com que a velocidade do jogo aumenta.
        self.speedup_scale = 1.2

        # A taxa com que os pontos para cada alienígena aumentam.
        self.score_scale = 1.5

        # Inicializa os valores dos atributos que devem mudar no curso do jogo.
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        ''' Inicializa as configurações que mudam no decorrer do jogo. '''

        self.ship_speed_factor = 1.5 # Velocidade da espaçonave.
        self.bullet_speed_factor = 3 # Velocidade dos porjéteis.
        self.alien_speed_factor = 1 # Velocidade dos alienígenas.

        # Fleet_direction igual a 1 representa a direita; -1 representa a esquerda.
        self.fleet_direction = 1 # Faz os alienígenas sempre se moverem para a direita no início de um jogo.

        # Pontuação.
        self.alien_points = 50 # Pontuação que o jogador recebe ao acertar um disparo em um alienígena.
    
    def increase_speed(self):
        ''' Aumenta as configurações de velocidade e os pontos para cada alienígena. '''

        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale) # Pegar apenas a parte inteira (arredonda para baixo).
    