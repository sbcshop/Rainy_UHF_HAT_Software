''' Demo Code Display Text to onboard TFT Display '''
import os
import sys
sys.path.append("examples/lib")
from PIL import Image, ImageDraw, ImageFont
from lib import display_1inch14
from time import sleep

# Set up the font paths
font1 = ImageFont.truetype("font/Font00.ttf", 25)
font2 = ImageFont.truetype("font/Font00.ttf", 16)
font3 = ImageFont.truetype("font/Font02.ttf", 25)

# Initialize the LCD display
disp = display_1inch14.lcd_display()
disp.Init()
disp.clear()

# Create a new image with white background
image = Image.new("RGB", (disp.width,disp.height), "BLACK")

# Draw some text on the image
draw = ImageDraw.Draw(image)
draw.text((10, 5), "Rainy UHF", font=font1, fill="YELLOW")
draw.text((10, 60), "HAT", font=font1, fill="BLUE")
disp.ShowImage(image)
sleep(5)

draw.text((10, 60), "HAT", font=font1, fill="BLACK")
draw.text((10, 60), "for RaspberryPi", font=font1, fill="BLUE")
disp.ShowImage(image)
sleep(2)

