from the_game_window import *
import os
import pygame
from the_constants import *

pygame.font.init()

win=pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('The Enemy Platformer Game')

clock=pygame.time.Clock()

game_window = the_game_window("images","main_chracter-removebg-preview.png",0,500-60,win)
# Main Loop

run=True

while run:
    clock.tick(FPS)

    events = pygame.event.get()
    key_pressed = pygame.key.get_pressed()
    for event in events:
        if event.type==pygame.QUIT:
            run=False


    win.fill((WHITE))
    game_window.draw()
    game_window.move_character(key_pressed)
    pygame.display.update()

pygame.quit()
