import serial
import binascii
import time
import array
from time import sleep

# Command Constants
START_BYTE = 'AA00'
END_BYTE = 'DD'
HARDWARE_VERSION_CMD = '0300010004'
SINGLE_READ_CMD = '22000022'
MULTIPLE_READ_CMD = '27000322271083'
STOP_READ_CMD = '28000028'
TRANSMIT_POWER_CMD = 'B70000B7'
EU_REGION = '070001030B'
US_REGION = '070001020A'

read_flag = False

class UHFMODULE():
    def __init__(self,port='/dev/ttyS0',baudrate=115200):
        self.uart = serial.Serial(port=port,baudrate = baudrate,
                      parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,
                      bytesize=serial.EIGHTBITS,timeout=1)
        self.uart.flush()
        
    def send_command(self, command):
        # Send a formatted command to the UHF module
        command_str = "".join(command)
        command_bytes = binascii.unhexlify(command_str)
        self.uart.write(command_bytes)
            
    def get_hardware_version(self):
        # Retrieve the hardware version of the UHF module
        self.send_command([START_BYTE, HARDWARE_VERSION_CMD, END_BYTE])
        sleep(0.1)
        response = self.uart.read(24)
        start_index = response.find(b'\xaa\x01\x03\x00\x10\x10')
        version_data = response[start_index+6:29]
        version_str = str(version_data[1:-2])
        return version_str[2:-1]
    
    def read_single_tag(self):   
        # Perform a single polling read operation
        self.send_command([START_BYTE, SINGLE_READ_CMD, END_BYTE])
        sleep(0.1)
        response = self.uart.readline()
        
        if response and len(response) > 22:
            if response[0] != 0xAA or response[23] != 0xDD or response[1] != 0x02:
                return None
            return ['{:02x}'.format(byte) for byte in response]
        else:
            print("Tag reading failed")
    
    def read_multiple_tags(self):
        # Perform a continuous multiple polling read operation, to stop exectue stop_read
        global read_flag
        if not read_flag:
            self.send_command([START_BYTE, MULTIPLE_READ_CMD, END_BYTE])
            sleep(0.5)
            read_flag = True
        
        response = self.uart.read(1024)
        if response and len(response) > 22:
            if response[0] != 0xAA or response[23] != 0xDD or response[1] != 0x02:
                return None
            return ['{:02x}'.format(byte) for byte in response]
    
    def stop_read(self):
        # Stop the tag reading operation
        global read_flag
        read_flag = False
        self.send_command([START_BYTE, STOP_READ_CMD, END_BYTE])
    
    def set_region(self, cmd):
        # Set the operating region
        if cmd=="EU":
            self.send_command([START_BYTE, EU_REGION, END_BYTE])
        elif cmd=="US":
            self.send_command([START_BYTE, US_REGION, END_BYTE])
            
        sleep(0.5)
        response = self.uart.readline()
        frame_byte = ['{:02x}'.format(byte) for byte in response]
        print(frame_byte)
        
        if frame_byte[2] == '07':
            print(cmd, "Region set successfully!")
        else:
            print("Region set failed!")
    
    def get_transmit_power(self):
        # Retrieve the current transmit power setting
        self.send_command([START_BYTE, TRANSMIT_POWER_CMD, END_BYTE])
        sleep(0.5)
        response = self.uart.read(24)
        frame_byte = ['{:02x}'.format(byte) for byte in response]
        if frame_byte:
            power_data = int("".join(frame_byte[5:-2]), 16)
            return f"{power_data / 100} dBm"
    
    def set_transmit_power(self, power_level):
        # Set the transmit power level (acceptable range: 15-26 dBm)
        hex_value = "0" + hex(power_level * 100)[2:]
        checksum = self.calculation("b60002" + hex_value)
        self.send_command([START_BYTE, "b60002", hex_value, checksum, END_BYTE])
        sleep(0.5)
        response = self.uart.readline()
        frame_byte = ['{:02x}'.format(byte) for byte in response]
        print(frame_byte)
        if frame_byte[2] == 'b6':
            print("Transmission power set successfully")
        else:
            print("Transmission power setting failed")
            
    def calculate_checksum(self,data):
        checksum = 0
        for byte in data:
            checksum += byte
        checksum_1 = (checksum) % 256
        return checksum

    def calculation(self,Data):
        bin_data1 = binascii.unhexlify(Data)
        chk_1 = (hex(self.calculate_checksum(bin_data1)))
        #print("checksum",chk_1)
        if len(chk_1) == 5:
            return str(chk_1[3:])
        elif len(chk_1) == 4:
                return str(chk_1[2:])
        else:
            return '0'+ str(chk_1[3:])
    
    def select_tag(self, epc_id):
        # Select a specific RFID tag using its EPC ID
        checksum = self.calculation("0C001301000000206000" + epc_id)
        self.send_command([START_BYTE, "0C001301000000206000", epc_id, checksum, END_BYTE])
        sleep(0.5)
        response = self.uart.readline()
        frame_byte = ['{:02x}'.format(byte) for byte in response]
        if frame_byte[2] == '0c':
            print("Tag selected successfully")
        else:
            print("Tag selection failed")
    
    def read_tag_memory(self, memory_bank):
        # Read data from a specific memory bank of a selected RFID tag
        checksum = self.calculation("390009000000000" + str(memory_bank) + "00000008")
        self.send_command([START_BYTE, "390009000000000", str(memory_bank), "00000008", checksum, END_BYTE])
        sleep(0.5)
        response = self.uart.readline()
        
        if response:
            frame_byte = ['{:02x}'.format(byte) for byte in response]
            print(frame_byte)
            if frame_byte[2] == '39':
                print("Tag read successfully")
                return "".join(frame_byte[20:-2])
            else:
                print("Tag reading failed")
    
    def write_tag_memory(self, memory_bank, data):
        # Write data to a specific memory bank of a selected RFID tag
        checksum = self.calculation("490019000000000" + str(memory_bank) + "00000008" + data)
        self.send_command([START_BYTE, "490019000000000", str(memory_bank), "00000008", data, checksum, END_BYTE])
        sleep(0.5)
        response = self.uart.readline()
        if response:
            frame_byte = ['{:02x}'.format(byte) for byte in response]
            if frame_byte[2] == '49':
                print("Tag writing successful")
                return "Success"
            else:
                print("Tag writing failed")

