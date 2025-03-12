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
 

def frame_content(data):
    frames = []
    current_frame = []

    for value in data:
        if value == 'aa':  
            current_frame = ['aa']  # Start new frame
        elif value == 'dd' and current_frame:
            current_frame.append('dd')  # End frame
            frames.append(current_frame)  # Store complete frame
            current_frame = []  # Reset for next frame
        else:
            if current_frame:  # Only add if inside a frame
                current_frame.append(value)

    # Print all extracted tag frames
    for i, frame in enumerate(frames):
        if 'ff' not in frame:
            print(f"Frame {i+1}: {frame}")


while True:
    recv = uhf.read_multiple_tags()
    print(recv)
    if recv is not None:
        beep()
        frame_content(recv)
    sleep(0.01)
    