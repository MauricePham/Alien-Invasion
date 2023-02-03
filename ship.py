import pygame
from pygame.sprite import Sprite


def blitme(self):
        self.screen.blit(self.image, self.rect)

class Moon:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect(topleft=(150, 300))
        self.image = pygame.image.load('images/moon.bmp')
        self.rect = self.image.get_rect()
        self.rect.bottomleft = self.screen_rect.bottomleft
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
class Ship(Sprite):
    
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False
    
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
       


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            self.rect.x -= 1
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

        

   