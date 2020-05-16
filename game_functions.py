import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
import sound_effects as se
from pygame.constants import *

def updateFile(stats):
    f = open('scores.txt','r') # Abre o arquivo no modo de leitura.
    file = f.readlines() # Lê todas as linhas como uma lista.
    last = int(file[0]) # Obtém a primeira linha do arquivo.

    if last < int(stats.score): # Vê se a pontuação atual é maior que a melhor anterior.
        f.close() # Fecha / Salva o arquivo.
        file = open('scores.txt', 'w') # Reabre-o no modo de gravação.
        file.write(str(stats.score)) # Escreve a melhor pontuação.
        file.close() # Fecha / Salva o arquivo.

        return stats.score
               
    return last

def check_keydown_events(event, ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    ''' Responde a pressionamentos de tecla. '''
    if event.key == K_RIGHT:
        # Move a espaçonave para a direita.
        ship.moving_right = True 
        ''' Quando o jogador pressiona a seta para a direita em vez de mudar a posição 
            da espaçonave de forma direta. '''

    elif event.key == K_LEFT:
        # Move a espaçonave para a esquerda.
        ship.moving_left = True

    elif event.key == K_UP:
        # Move a espaçonave para cima.
        ship.moving_up = True

    elif event.key == K_DOWN:
        # Move a espaçonave para baixo.
        ship.moving_down = True

    # A espaçonave atira.
    elif event.key == K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

    elif event.key == K_p:
        start_game(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

    elif event.key == K_q:
        updateFile(stats)
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    ''' Dispara um projétil se o limite ainda não foi alcançado. '''

    # Cria um novo projétil e o adiciona ao grupo de projéteis.
    if len(bullets) < ai_settings.bullets_allowed:
        ''' Se len(bellets) for menor que três, criamos  um novo projétil. Se for mior, 
            nada acontecerá a barra de espaço qundo pressionada. Nesse caso, só é capaz de disparar
            projetéis somente em grupos de três. '''
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        se.bullet_sound.play() # Som do laser.

def check_keydup_events(event, ship):
    ''' Responde a solturas de tecla. '''
    if event.key == K_RIGHT:
        ship.moving_right = False

    elif event.key == K_LEFT:
        ship.moving_left = False

    elif event.key == K_UP:
        ship.moving_up = False

    elif event.key == K_DOWN:
        ship.moving_down = False

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    ''' Responde a eventos de pressionamento de teclas e de mouse. '''
    
    for event in pygame.event.get():
        ''' Observa eventos de teclado e de mouse. '''
        if event.type == QUIT:
            sys.exit()

        # Quando o jogador pressionar as teclas.
        elif event.type == KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats,sb, play_button, ship, aliens, bullets)

        # Quando o jogador solta as teclas.
        elif event.type == KEYUP:
            check_keydup_events(event, ship)

        elif event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def start_game(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):

     # Oculta o cursor do mouse.
    pygame.mouse.set_visible(False)
    ''' Passar False para set_visible() diz ao Pygame para ocultar 
        o cursor quando o mouse estiver sobre a janela do jogo. '''

    # Reinicia as configurações do jogo.
    ai_settings.initialize_dynamic_settings()
    
    # Reinicia os dados estatistícos do jogo. 
    stats.reset_stats()
    stats.game_active = True

    # Reinicia as imagens do pinel de pontuação.
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()

    # Esvazia a lista de alienígenas e de projéteis.
    aliens.empty()
    bullets.empty()

    # Cria uma nova frota e centraliza a espaçonave.
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    ''' Inicia um novo jogo quando o jogador clicar em play. '''

    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        ''' O jogo será reiniciado somente se Play for clicado e o jogo não estiver ativo no momento. '''

        start_game(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
            
def update_screen(ai_settings, screen, stats, sb, ship, aliens, background, bullets, play_button):
    '''  Atualiza as imagens na tela e altera para a nova tela. '''
    
    # Redesenha todos os projéteis atrás da espaçonave e dos alienígenas a cada passagem pelo laço.
    screen.fill([230, 230, 230])
    screen.blit(background.image, background.rect)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme() # Faz a espaçonave aparecer na tela.
    aliens.draw(screen) # Desenha cada alienígena do grupo na tela.

    # Desenha a informação sobre pontuação.
    sb.show_score()

    # Desenha o botão Play se o jogo estiver inativo.
    if not stats.game_active:
        play_button.draw_button()

    # Deixa a tela mais recente visível.
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    ''' Atualiza a posição dos projetéis e se livra dos projéteis antigos. '''

    # Atualiza as posiçôes dos projéteis de acordo com a flag de movimento da espaçonave.
    bullets.update()

    # Livra-se dos projéteis que desapareceram.
    for bullet in bullets.copy():
        ''' Não devemos remover itens de uma lista ou de um gruo em um laço for, portanto
            precisamos usar uma cópia do grupo no laço. '''
        if bullet.rect.bottom <= 0:
            ''' Verificamos cada projétil para ver se ele desapareceu por ter ultrapassado
                a parte superior da tela. '''
            bullets.remove(bullet)
    ''' Mostra quantos projéteis existem no momento no jogo e conferir se estão sendo apagados. '''
    #print(len(bullets))

    ''' Verifica se algum projétil atingiu os alieníginas. Em caso afirmativo, livra-se
        do pojétil e do alienígena. '''
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    ''' Responde a colisôes entre projéteis e alienígenas. '''

    # Remove qualquer projétil e alienígena que tenham colidido.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)

        sb.prep_score()
        check_high_score(stats, sb)
        se.alien_sound.play() # Som da colisão do laser com os alienígenas.

    if not aliens:
        ''' Destrói os projéteis existentes, aumenta a velocidade do jogo e cria uma nova frota. '''

        # Se a frota toda for destruída, inicia um novo jogo.
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ai_settings.increase_speed()

        # Adicionando o level.
        stats.level += 1
        sb.prep_level()
        
def check_high_score(stats, sb):
    ''' Verifica se há uma nova pontuação máxima. check_high_score() aceita dois
        parâmetros: stats e sb. Ela usa stats para verificar a pontuação atual e a
        pontuação máxima, e precisa de sb para modificar a imagem da pontuação máxima 
        quando for necessário. '''

    if stats.score > stats.high_score: # Verifica a pontuação atual com a pontuação máxiam.
        stats.high_score = stats.score # Pontuação máxima recebe a pontução atual.
        sb.prep_high_score() # Atualiza a imagem com a pontuação máxima.

def get_number_aliens_x(ai_settings, alien_width):
    ''' Determina o tamanho de alieníginas que cabem em uma linha. '''

    ''' Calcula o espaço horizintal disponível para os alienígenas e o 
        número de alienígenas que cabem nesse espaço. '''
    available_space_x = ai_settings.screen_width - 2 * alien_width 
    number_aliens_x = int(available_space_x / (2 * alien_width)) # Grante um número inteiro de alienígenas.

    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    ''' Determina o número de linhas com alienígenas que cabem na tela. '''

    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))

    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # Criaum alienígena e o posiciona na linha
    # O espaçamento entre os alienígenas é igual à largura de um alienígena.
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width # Adquirimos a largura do alienígina a partir do seu atributo rect.
    alien.x = alien_width + (2 * alien_width * alien_number) # Multiplica por 2 o tamanho do alienígena para considerar o espaço vazio.
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number 
    # Muda o valor da coordenada y de um alienígena quando ele não estiver na primeira linha.
    aliens.add(alien) # Adiciona cada novo alienígina ao grupo aliens.

def create_fleet(ai_settings, screen, ship, aliens):
    ''' Cria uma frota completa de alienígenas. '''

    # Cria um alienigena e calcula o número de alienígenas em uma linha.
    alien = Alien(ai_settings, screen) # Cria um alienigena.
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    # Cria a frota de alieníginas.
    for row_number in range (number_rows): # Conta de 0 até o número de linhas que queremos.
        for alien_number in range(number_aliens_x): # Cria os alienígenas em uma linha.
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    ''' Responde apropriadamente se algum alienígena alcançar uma borda. '''

    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    ''' Faz toda a frota descer e mudar a sua direção. '''

    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    ''' Responde ao fato de a espaçonave ter sido atingida por um alienígena. '''

    se.alien_sound.play() # Som da colisão do alienígena com parte inferior da tela e com a espaçonave.

    if stats.ships_left > 0: 
        ''' testa se o jogador tem pelo menos uma espaçonave restante. '''

        # Decrementa ships_left.
        stats.ships_left -= 1 # O número de espaçonave restante é reduzida de 1, e depois disso esvaziamos
        # os grupos aliens e bullets.

        # Atualiza o painel de pontuações(espaçonaves que restam ao jogador).
        sb.prep_ships()

        # Esvazia a lista de alieníginas e de projéteis.
        aliens.empty()
        bullets.empty()

        # Cria uma nova frota e centraliza a espaçonave.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Faz uma pausa.
        sleep(0.7)

    else:
        ''' Se o jogador não tiver nenhuma espaçonave restante, definimos game_active como False. '''
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    ''' Verifica se algum alienígena alcançou a parte inferior da tela. '''

    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom: # Verifica se o lienígena alcaçou a aprte inferio da tela.
            # Trata esse do mesmo modo que é feito quando a espaçonave é atingida.
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break

def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    ''' Verifica se a frota está em uma das bordas e então atualiza as posições 
        de todos os alienígenas da frota. '''

    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Verifica se houve colisões entre alienígenas e a espaçonave.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)

    # Verifica se há algum alienígena que atingiu a parte inferior da tela.
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)
