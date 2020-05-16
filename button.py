import pygame.font
''' Pygame.font permite que o Pygame renderize um texto na tela. '''

class Button():
    ''' escreveremos uma classe Button para criar um retângulo preenchido e que tenha um rótulo '''

    def __init__(self, ai_settings, screen, msg):
        ''' Inicializa os atributos do botão. '''

        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Define as dimensôes e as propriedades do botão.
        self.width, self.height = 200, 50 # Dimensões do botão.
        self.button_color = (20, 40, 130) # Cor do botão.
        self.text_color = (255, 255, 255) # Renderiza o texto em branco.
        self.font = pygame.font.SysFont(None, 48) # Prepara o atributo font para renderiza o texto.
        # 48 é o tamanho do texto e None usa uma fonte default.

        # Constrói o objeto rect do botão e o centraliza.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # A mensagem do botão deve ser preparada apenas uma vez.
        self.prep_msg(msg)
        ''' O Pygame trabalha com textos renderizando a string que você quer exibir como uma imagem. '''

    def prep_msg(self, msg):
        ''' Transforma msg em imagem renderizada e centraliza o texto no botão. '''

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        ''' Desenha um botão em branco e, em seguida, desenha a mesnagem. '''

        self.screen.fill(self.button_color, self.rect) # Desenha a parte retângualr do botão.
        self.screen.blit(self.msg_image, self.msg_image_rect) # Desenha a imagem do texto na tela.
