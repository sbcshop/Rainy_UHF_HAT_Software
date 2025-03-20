''' Demo to perform Multiple Polling operation for MultiTag Detection '''
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


# Store unique EPCs
unique_epcs = set()

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

    # Extract and store only unique EPCs
    for i, frame in enumerate(frames):
        if 'ff' not in frame and len(frame) > 10:  # Ensure it's a valid EPC frame
            epc = "".join([byte.zfill(2) for byte in frame[8:-2]])  # Format EPC properly
            
            if epc not in unique_epcs:  # Check if EPC is new
                unique_epcs.add(epc)    # Store unique EPC
                print(f"New EPC Detected: {epc}")  # Print only new EPCs

while True:
    recv = uhf.read_multiple_tags()
    #print(recv)
    if recv is not None:
        beep()
        frame_content(recv)
        break
    sleep(0.01)

uhf.stop_read()  #make sure to perform stop read operation after every Multiread operation
print("Done")
