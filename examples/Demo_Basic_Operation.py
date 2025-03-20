''' Code to perform Basic Rainy UHF operations '''

#import required modules
from lib.rainy_uhf import UHFMODULE
from PIL import Image, ImageDraw, ImageFont
from lib import display_1inch14
from time import sleep
import RPi.GPIO as GPIO
import os
import sys
sys.path.append("examples/lib")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

font1 = ImageFont.truetype("font/Font00.ttf", 25)
font2 = ImageFont.truetype("font/Font00.ttf", 16)

disp = display_1inch14.lcd_display()
disp.clear()
disp.Init()   # initialize display

enable_pin = 12
GPIO.setup(enable_pin,  GPIO.OUT)
GPIO.output(enable_pin, GPIO.HIGH)  #Activate Rainy UHF module, HIGH - to enable, LOW - to disable

baudrate = 115200 #default baudrate of Rainy UHF module
port = '/dev/ttyS0' # use for RPi 4 and previous version
#port = '/dev/ttyAMA0' # uncomment to use with  RPi 5

uhf = UHFMODULE(port,baudrate) # create instance for UHF module

# Set the UHF module's operating region, command should be executed only once  
# Available options:  
# "US" -> For the United States (902-928 MHz)  
# "EU" -> For the European region (865-868 MHz)
# You get reduce working range if incorrect region set 
uhf.set_region("EU")

# show hardware version and transmit power on display
image = Image.new("RGB", (disp.width,disp.height), "BLACK")
draw = ImageDraw.Draw(image)

response1 = uhf.get_hardware_version() #get hardware version of UHF module
print("Hardware Version: ", response1)

draw.text((10, 5),response1 , font=font1, fill="YELLOW")
disp.ShowImage(image)

# Set the transmit power level (acceptable range: 15-26 dBm)
uhf.set_transmit_power(21) 

response2 = uhf.get_transmit_power() #get power value
print("Transmit Power: ",response2)

draw.text((10, 60), response2, font=font1, fill="YELLOW")
disp.ShowImage(image)
sleep(2)



