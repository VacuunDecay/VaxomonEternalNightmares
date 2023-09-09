import pygame


class Sprite():
    

    def __init__(self, imagePath, scrn):
    
        self.imgae = pygame.image.load(imagePath)
        self.scrn = scrn

    def draw(self,  x, y):
        self.cords = (x, y)
        self.scrn.blit(self.imgae, self.cords)

