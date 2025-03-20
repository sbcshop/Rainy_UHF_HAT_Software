'''
Demo code to perform UHF Tags Memory write operation
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
Memory Bank : only writable memory can be used for memory write operation
1 - EPC  --> Read/Write
3 - USER --> Read/Write

2Byte = 1 Word for Rainy UHF Module
For Ease Write operation we have set 8 Word size (16 Byte) data size in library, So follow below configuration:

User Memory => 
- For Data write in user memory you can create random data of length 8 Word
  example,
  data_value = 00000000000000000000000000000012  <= pass for write

EPC Memory =>
- Use Tag Memory Read [Memory Bank - 1] operation first to get ResponseFrame
- For example,
  if EPC is e28068940000501d93f2b125, you will get below using read operation
  ResponseFrame = '30003400e28068940000501d93f2b125'
  3000, 3400,  [e28068940000501d93f2b125] (old EPC)
  
  Data Frame with New EPC,
  3000, 3400, [e28068940000501d93f2b125] (new EPC)
  data_value = 30003400e28068940000501d93f2b127  <= pass this for write

'''

memory_bank = '1' # Change for corresponding Memory Write operation

''' Uncomment and provide data interested to write into memory '''
#data_value = "00000000000000000000000000000015"  # Random data for storing into memory 3
data_value =   "a66d3400c7059afb1a99bd25ef7853d7" # Data with EPC value for memory 1
#print(data_value)

# Select corresponding Tag, Change with EPC of card on which write needs to perform
uhf.select_tag("c7059afb1a99bd25ef7853d6")  

response = None

while 1:
    response = uhf.write_tag_memory(memory_bank, data_value)  #Tag Memory Data Write
    if response is not None:
        beep()
        print("Data= ",response)
        break
    sleep(0.1)
