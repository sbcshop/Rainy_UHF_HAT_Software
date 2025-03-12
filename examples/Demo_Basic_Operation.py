''' Code to perform Basic Rainy UHF operations '''

#import required modules
from lib.rainy_uhf import UHFMODULE
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

enable_pin = 12
GPIO.setup(enable_pin,  GPIO.OUT)

#Activate Rainy UHF module, HIGH - to enable, LOW - to disable
GPIO.output(enable_pin, GPIO.HIGH)


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


response = uhf.get_hardware_version() #get hardware version of UHF module
print("Hardware Version: ", response)

# Set the transmit power level (acceptable range: 15-26 dBm)
uhf.set_transmit_power(26) 

response = uhf.get_transmit_power() #get power value
print("Transmit Power: ",response)

    
    

            
    


