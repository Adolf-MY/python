__author__ = 'Frank'
import pygame
from pygame.locals import  *
from sys import  exit
background_image_filename = 'sushiplate.jpg'
pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
background = pygame.image.load(background_image_filename).convert()

'''x,y=0,0
move_x,move_y=0,0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -1
            elif event.key == K_RIGHT:
                move_x = 1
            elif event.key == K_UP:
                move_y = -1
            elif event.key == K_DOWN:
                move_y = 1
        elif event.type == KEYUP:
            move_x = 0
            move_y = 0
        x +=move_x
        y +=move_y
        screen.fill((0,0,0))
        screen.blit(background,(x,y))
        pygame.display.update()'''
#my_event = pygame.event.Event(KEYDOWN,key = K_SPACE,mod=0,unicode=u' ')
#my_event = pygame.event.Event(KEYDOWN,{"key":K_SPACE,"mod":0,"unicode":" "})
#pygame.event.post(my_event)

CATONKEYBOARD = USEREVENT+1
my_event = pygame.event.Event(CATONKEYBOARD,message = "Bad cat!")
pygame.event.post(my_event)
for event in pygame.event.get():
    if event.type == CATONKEYBOARD:
        print event.message