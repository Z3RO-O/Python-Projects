# SPOT THE DIFFERENCE GAME
import pygame

# initialize pygame framework
pygame.init()

# Game Window
Window_Width = 1200
Window_Height = 800
Display_surface = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption('SPOT THE DIFFERENCE')

# CONSTANTS
Game_Folder = 'd:/Code/PycharmProjects/spot_the_difference/'
BLUE = pygame.Color(0, 0, 255)
RED = pygame.Color(255, 0, 0)

# Game Assets
background_image = pygame.image.load(Game_Folder + 'spot_the_difference.jpg')

# Game Data Structures Values
chances = 10
click_points = []
actual_points = [()]

FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
pygame.quit()
