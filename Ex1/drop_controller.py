import pygame
import pygame.locals

class Controller:

    def __init__(self):
        self.running = True
        self.left = False
        self.right = False

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.left = True
                if event.key == pygame.K_RIGHT:
                    self.right = True
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.left = False
                if event.key == pygame.K_RIGHT:
                    self.right = False
        if self.left and self.right:
            self.left = False
            self.right = False

controller = Controller()