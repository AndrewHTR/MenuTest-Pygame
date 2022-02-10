import pygame, sys
from pygame.locals import *

# Iniciando Pygame:
pygame.init()

# Janela:
WINDOWWIDTH = 600
WINDOWHEIGHT = 400
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption("Menu Test")

clock = pygame.time.Clock()

# Função para faciliar o uso do Texto:
font = pygame.font.SysFont(None, 50)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Função principal:
def main():
    while True:
        screen.fill((0, 0, 0))

        draw_text("Main", font, (255, 255 ,255), screen, 15, 15)
        # Pegando posição do mouse para saber se ele colidiu com o botão:
        mouse = pygame.mouse.get_pos()

        # Criando a colisão dos botões:
        botao1 = pygame.Rect(60,80,130,40)
        botao2 = pygame.Rect(60,150,130,40)
        
        # Desenhando colisão dos botões:       
        pygame.draw.rect(screen, (0, 0, 0), botao1)
        pygame.draw.rect(screen, (0, 0, 0), botao2)

        draw_text("Game", font, (225, 255, 255), screen, botao1.topleft[0] + 15, botao1.topleft[1] + 3)
        draw_text("Option", font, (225, 255, 255), screen, botao2.topleft[0] + 8, botao2.topleft[1] + 2)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Pegar evento de colisão e clique do mouse para acionar a função:
            if event.type == MOUSEBUTTONDOWN:
                if botao1.collidepoint(mouse):
                    if event.button == 1:
                        game()
                if botao2.collidepoint(mouse):
                    if event.button == 1:
                        option()
        pygame.display.update()
        clock.tick(60)

# Tela de opções:
def game():
    running = True
    # Looping para manter a tela aberta apenas quando o usuario apertar no botão e reduzir o uso de memoria:
    while running:
        screen.fill((0, 0, 0))
        draw_text("Game", font, (255, 255 ,255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_q:
                    running = False
            
        pygame.display.update()
        clock.tick(60)

# Tela de opções:
def option():
    running = True
    # Looping para manter a tela aberta apenas quando o usuario apertar no botão e reduzir o uso de memoria:
    while running:
        screen.fill((0, 0, 0))
        draw_text("Option", font, (255, 255 ,255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_q:
                    running = False
            
        pygame.display.update()
        clock.tick(60)
        
main()
