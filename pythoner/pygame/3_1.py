__author__ = 'Frank'
import pygame
from pygame.locals import  *
from sys import  exit
background_image_filename = 'sushiplate.jpg'
screen_size = (640,480)
pygame.init()
screen = pygame.display.set_mode(screen_size,RESIZABLE,32)
background = pygame.image.load(background_image_filename).convert()
while True:
    event = pygame.event.wait()
    if event.type == QUIT:
        exit()
    if event.type == VIDEORESIZE:
        screen_size = event.size
        screen = pygame.display.set_mode(screen_size,RESIZABLE,32)
        pygame.display.set_caption("window resized to"+str(event.size))
    screen_width,screen_height = screen_size
    for y in range(0,screen_height,background.get_height()):
        for x in range(0,screen_width,background.get_width()):
            screen.blit(background,(x,y))
    pygame.display.update()