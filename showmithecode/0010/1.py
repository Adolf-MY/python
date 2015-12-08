#coding=utf8
__author__ = 'Frank'
from PIL import Image,ImageFont,ImageDraw,ImageFilter
import random,string

IMAGE_MODE = 'RGB'
IMAGE_BG_COLOR = (255,255,255)
Image_Font = 'E:/python/Users/Frank/PycharmProjects/python/python/showmithecode/0010/arial.ttf'

a= string.letters
text = ''.join(random.choice(a) for i in range(4))
print text

def colorRandom():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width,height,chance= 400,200,2

im = Image.new(IMAGE_MODE,(width,height),IMAGE_BG_COLOR)
draw = ImageDraw.Draw(im)
for w in xrange(width):
    for h in xrange(height):
        if chance < random.randint(1,100):
            draw.point((w,h),fill=colorRandom())
font =ImageFont.truetype(Image_Font,80)
font_width,font_height = font.getsize(text)
strs_len = len(text)
x = (width - font_width)/4
y = (height - font_height)*2/5
for i in text:
    draw.text((x,y),i,colorRandom(),font)
    x+=font_width/strs_len+(width-font_width)/6
im.show()