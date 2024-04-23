import os, sys,math
from PIL import Image, ImageDraw, ImageFont

def getChar(ascii_char):
    return charArray[math.floor(ascii_char*interval)]


chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1] #reverse
charArray = list(chars)
charLength= len(charArray)
interval = charLength/256

scale = 0.3

charWidth = 10
charHeight = 18

image_file = Image.open("./input/hanekawa.jpg")

ascii_art = open("./output/output.txt","w")

fnt = ImageFont.truetype("./Courier.ttf",22)

width,height = image_file.size
image_file = image_file.resize((int(scale*width), int(scale*height*(charWidth/charHeight))), Image.NEAREST)
width,height = image_file.size

pixels = image_file.load()

ascii_image = Image.new("RGB",(charWidth*width,charHeight*height),color = (0,0,0))
draw = ImageDraw.Draw(ascii_image)

print(width,height)

for i in range(height):
    for j in range(width):
        r,g,b = pixels[j,i]
        brightness_value = int(r/3 + g/3 + b/3)
        pixels[j,i] = (brightness_value,brightness_value,brightness_value)
        ascii_art.write(getChar(brightness_value))
        draw.text((j*charWidth,i*charHeight),getChar(brightness_value),font=fnt,fill=(r,g,b))
    ascii_art.write("\n")


ascii_image.save("./output/ascii_art4.jpg")