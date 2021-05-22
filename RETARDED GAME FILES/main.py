

import sys

import pygame, os
import game_module as gm

os.environ['SDL_VIDEO_CENTERED'] = '1'          #centrowanie okna
pygame.init()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('game base')

screen = pygame.display.set_mode(gm.SIZESCREEN)

clock = pygame.time.Clock()


#game controlls
import pygame_controller







pygame.display.update()
clock.tick(60)

    #sprites
    #movement
    #guns and bullets
#rocks
    #how they die
#big head
    #how it acts
#ui
#głowna pętla gra
window_open = True
while window_open:
    #screen.fill(gm.LIGHTBLUE)
    screen.blit(gm.BACKGROUND, (0,0))
    #pętla zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_open = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False

        player.get_event(event)
    #pionts