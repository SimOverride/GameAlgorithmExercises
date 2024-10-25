import pygame
import random
from drop_controller import controller
from typing import List

WINDOW_WIDTH  = 400
WINDOW_HEIGHT = 600

class Platform:
    ''' Platforms start from the bottom of the screen and move up.  Each
        has a gap through which the Avatar can fall.
    '''
    
    # Class variables!
    delay = 2000         # New platform starts up every 2000 microseconds
    fastest_delay = 700  # and decreases until they are coming every 700 mseconds
    time_of_last_platform = 0
    THICKNESS = 10
    GAP_WIDTH = 40
    speed = 3
    
    def __init__(self):
        self.y = WINDOW_HEIGHT
        self.gap_x = random.randint(0, WINDOW_WIDTH - Platform.GAP_WIDTH)
        Platform.time_of_last_platform = pygame.time.get_ticks()
        Platform.delay = max(Platform.fastest_delay, Platform.delay - 50)
        
    def collision(self, avatar_x, avatar_y, avatar_width):
        ''' Return True if the avatar would be drawn within the solid portion
            of this platform.
        '''
        assert avatar_x >= 0
        assert avatar_x < WINDOW_WIDTH
        assert avatar_y >= 0
        assert avatar_y < WINDOW_HEIGHT
        if avatar_y < self.y or avatar_y > self.y + Platform.THICKNESS:
            return False
        # If avatar is over the gap, then no collision
        if avatar_x < self.gap_x:
            return True
        if avatar_x + avatar_width > self.gap_x + Platform.GAP_WIDTH:
            return True
        return False
        
    def update(self):
        ''' Platform just needs to move up with each update.
        
            Returns: False when the platform's bottom is no longer viewable.
        '''
        self.y -= Platform.speed
        return self.y > -Platform.THICKNESS

platforms : List[Platform] = []

class RedBox:
    HEIGHT = 25
    WIDTH = 10

    def __init__(self):
        self.x = WINDOW_WIDTH / 2 - self.WIDTH / 2
        self.y = 1
        self.vx = 5
        self.vy = 3

    def update(self):
        if controller.left:
            self.x = max(0, self.x - self.vx)
        if controller.right:
            self.x = min(self.x + self.vx, WINDOW_WIDTH - self.WIDTH)
        bottom_left_y = self.y + self.HEIGHT - 1
        riding = None
        for platform in platforms:
            if platform.collision(self.x, bottom_left_y, self.WIDTH):
                riding = platform
                break
        if riding:
            bottom_left_y = riding.y
            self.y = bottom_left_y - self.HEIGHT        
        else:
            self.y += self.vy

player = RedBox()