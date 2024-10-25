import pygame
from drop_model import Platform, WINDOW_WIDTH, platforms, player

class Drawer:

    def __init__(self, surface):
        self.surface = surface

    def draw_platform(self, platform):
        ''' Draw the platform.
        '''
        pygame.draw.rect(self.surface,  # draw the platform in white
                         (255,255,255),
                         (0,platform.y, WINDOW_WIDTH, Platform.THICKNESS)
                        )
        pygame.draw.rect(self.surface,  # draw the gap in black
                         (0,0,0),
                         (platform.gap_x, platform.y, Platform.GAP_WIDTH, Platform.THICKNESS)
                        )
        
    def draw_player(self, player):
        pygame.draw.rect(self.surface, (255,0,0), (player.x, player.y, player.WIDTH, player.HEIGHT))

    def clear(self):
        self.surface.fill((0, 0, 0))

    def update(self):
        for platform in platforms:
            self.draw_platform(platform)
        self.draw_player(player)
        pygame.display.update()