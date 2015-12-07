#coding=utf8
__author__ = 'Frank'
from PIL import Image,ImageFont,ImageDraw,ImageFilter
import random,string

IMAGE_MODE = 'RGB'
IMAGE_BG_COLOR = (255,255,255)
Image_Font = 'arial.tff'

a= string.letters
text = ''.join(random.choice(a) for i in range(4))
print text

def colorRandom():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width,height,chance= 400,200,2

im = Image.new(IMAGE_MODE,(width,height),IMAGE_BG_COLOR)



