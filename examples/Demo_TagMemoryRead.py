'''
Code to perform read operation from Memory of UHF Tags,
Reserved, EPC, TID and User are different memory options available
'''
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
    
    
'''
Memory Bank 
1 - EPC  --> Read/Write
2 - TID  --> Only readable
3 - USER --> Read/Write
'''
memory_bank = '3' # Change for corresponding Memory Read operation

response = None

# Select corresponding Tag, Change with EPC of card whose memory needs to be read
uhf.select_tag("e28068940000501d93f2b125")  

while 1:
    response = uhf.read_tag_memory(memory_bank)  #Tag Memory Data read
    print("ResponseFrame:",response)
    if response is not None:
        beep()
        if memory_bank == '1':   # Response adjusted as per Tag data received
            print("EPC= ",response[8:])
        if memory_bank == '2':
            print("TID= ",response[:-8])
        if memory_bank == '3':
            print("Data= ",response)
        break
    sleep(0.1)

    

            
    


