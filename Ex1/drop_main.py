import pygame
from drop_model import Platform, RedBox, platforms, player, WINDOW_WIDTH, WINDOW_HEIGHT
from drop_view import Drawer
from drop_controller import controller

def main():
    pygame.init()
    surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    drawer = Drawer(surface)

    pygame.display.set_caption('Drop!')
    start_time = pygame.time.get_ticks()

    while controller.running:
        pygame.time.Clock().tick(30)
        drawer.clear()
         
        controller.check_events()

        done_platform = False
        for platform in platforms:
            if not platform.update():
                done_platform = platform
        if done_platform:
            platforms.remove(done_platform)
        if pygame.time.get_ticks() - Platform.time_of_last_platform > Platform.delay:
            new_platform = Platform()
            platforms.append(new_platform)

        player.update()

        if player.y < 0:
            break
        if player.y + player.HEIGHT > WINDOW_HEIGHT:
            break
        
        drawer.update()

    score = (pygame.time.get_ticks() - start_time)/1000
    print(f'You survived for {score} seconds')

if __name__ == "__main__":
    main()