import os
import pygame

from the_constants import CHARACTER_HEIGHT, CHARACTER_WIDTH

class the_game_window(object):
    def __init__(self,image_folder,image,character_x,character_y,surface):
        self.main_character = pygame.image.load(os.path.join(image_folder,image))
        self.main_character_shrinked = pygame.transform.scale(self.main_character,(CHARACTER_WIDTH,CHARACTER_HEIGHT))
        self.image = image
        self.character_x = character_x
        self.character_y = character_y
        self.surface = surface



    def draw(self):
        self.surface.blit(self.main_character_shrinked,(self.character_x,self.character_y))

    def move_character(self,key_pressed):
        if key_pressed[pygame.K_RIGHT]:
            self.character_x +=1

        if key_pressed[pygame.K_LEFT]:
            self.character_x -=1
        
        if key_pressed[pygame.K_UP]:
            self.character_y -=1

        if key_pressed[pygame.K_DOWN]:
            self.character_y +=1