import pygame
#from pygame import OPENGL, DOUBLEBUF
#from OpenGL.GL import *
from Scripts.MapGenerator import MapGenerator
from Scripts.Sprite import Sprite

class Game:
    @staticmethod
    def Init():
        Width = 1440
        Height = 690
        backGrondColor = (0, 12, 24)
        Title = "Vaxomon Eternal Nightmares"
        GameIsRunning = True
        pygame.init()
        pygame.display.set_caption(Title)
        Display = (Width, Height)
        scrn = pygame.display.set_mode(Display)

        clock = pygame.time.Clock()
        Map = MapGenerator(scrn)



        while GameIsRunning:

            #Event randeling
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            scrn.fill(backGrondColor)
            Map.draw()

            pygame.display.flip()
            clock.tick(60)

Game.Init()