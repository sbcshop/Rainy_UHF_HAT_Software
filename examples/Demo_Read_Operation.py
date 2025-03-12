''' Demo to perform Single Read operation '''
#import required modules
from lib.rainy_uhf import UHFMODULE
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

buzz=19
userLED = 26
enable_pin = 12

# Set pins as OUTPUT
GPIO.setup(enable_pin,  GPIO.OUT)
GPIO.setup(buzz,  GPIO.OUT)
GPIO.setup(userLED,  GPIO.OUT)

#Activate Rainy UHF module, HIGH - to enable, LOW - to disable
GPIO.output(enable_pin, GPIO.HIGH)


baudrate = 115200 #default baudrate of Rainy UHF module
port = '/dev/ttyS0' # use for RPi 4 and previous version
#port = '/dev/ttyAMA0' # uncomment to use with  RPi 5

uhf = UHFMODULE(port,baudrate) # create instance for UHF module

def beep():
    GPIO.output(userLED, GPIO.HIGH)
    GPIO.output(buzz, GPIO.HIGH)
    sleep(0.05)
    GPIO.output(userLED, GPIO.LOW)
    GPIO.output(buzz, GPIO.LOW)
    
def hex_to_signed_decimal(hex_number, bit_width):
    # Convert the hexadecimal number to a decimal integer
    decimal_number = int(hex_number, 16)
    
    # Calculate the maximum value for a signed integer of the given bit width
    max_value = 2 ** (bit_width - 1)
    
    # If the decimal number is greater than or equal to max_value, it is negative in two's complement
    if decimal_number >= max_value:
        decimal_number -= 2 ** bit_width

    return decimal_number

'''
Uncomment to set operating region, execute only once.
Options:
# "US" -> For the United States (902-928 MHz)  
# "EU" -> For the European region (865-868 MHz)
'''
#uhf.set_region("EU")

while True:
    recv = uhf.read_single_tag()
    #print(recv)
    if recv is not None:
        beep()
        epc = "".join(recv[8:20])
        rssi = hex_to_signed_decimal(recv[5],8)
        print(f"EPC: {epc}")
        print(f"RSSI: {rssi}dBm")
    sleep(0.01)
    
    

            
    

