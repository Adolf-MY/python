# -*- coding:utf-8 -*-
__author__ = 'Frank'
from  PIL import Image,ImageDraw,ImageFont
image = Image.open('E:/showcode/0000/t013ed0fe945a97d76f.jpg')
#image.show()
def add_num(image):
    draw = ImageDraw.Draw(image)
    myfont = ImageFont.truetype('E:/showcode/0000/Futura.ttf',20)
    fillcolor = "#ff0000"
    width,height=image.size
    draw.text((width-60,0),'99',font=myfont,fill=fillcolor)
    image.show()
add_num(image)