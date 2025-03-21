# Rainy UHF HAT Software

<img src="https://github.com/sbcshop/Rainy_UHF_HAT_Software/blob/main/images/FeatureBanner_RainyUHF_HAT.jpg">

UHF RFID technology with the Rainy HAT, an advanced RFID module engineered to integrate effortlessly with your Raspberry Pi board using standard 40 pin GPIOs header. Whether you're a hobbyist or a professional, this module offers a powerful and flexible solution for RFID applications, making it an ideal choice for exploring and deploying high-speed inventory tracking systems.

This github page provides a getting started guide and other working details for the Rainy UHF HAT for Raspberry Pi. 

### Features:
- **Standard 40 Pin Header** to seamlessly integrate with Raspberry Pi variants
- **1.14"** TFT Display for visual interaction
- **SMA Antenna port** to connect antenna of choice for increased range 1-20m
- Onboard **Buzzer** and **User** LED to show or add alert for any activity
- **Programmable Buttons** for adding additional control features
- **USB Type-C** interface for Rainy UHF module access
- **Jumper option** to switch mode, so you can use onboard UHF either with Raspberry Pi or direct access with software
 
### Specifications:
- **Microcontoller**  : Raspberry Pi 3, 4, 5, zero and compatible Boards
- **Supply Voltage:** 5V
- **Operating Pin:** 3.3V ~ 5V
- **Display Size**: 1.14"
- **Display Resolution**: 135x240 pixels
- **Communication Interface:** TTL (UART), Type C
- **Frequency:** EU 865-868MHz or US 902-928MHz
- **Protocol:** ISO 18000-6C (EPC Gen 2)
- **Read speed:** Multi-tag,1-60tags/second (depend on antenna/tag and application)
- **Read range:**- 1-20m (depend on tag, antenna and application)
- **Read/Write Capability:** Yes
- **RF Power Output:** 15-26 dBm(adjustable)
- **Cooling Method:** Air cooling (no external heat sink required)
- **Antenna port:** 1 port ,SMA
- **Estimated Antenna Range:** 
     - **3dBi Antenna:** 0-2m Range
     - **5.5dBi Antenna:** 0-5m Range
       
## Getting Started with Rainy UHF for ESP32
### Pinout:
<img src="https://github.com/sbcshop/Rainy_UHF_HAT_Software/blob/main/images/Rainy_UHF_HAT_Pinouts.jpg" width="" height=""> 

### Interfacing Details:
Following GPIO pins consumed when Rainy UHF HAT connected on Raspberry Pi,

<img src="https://github.com/sbcshop/Rainy_UHF_HAT_Software/blob/main/images/interfacing_info.png" width="440" height="345"> 

**You have two options to use Rainy UHF HAT,**
- _1) HAT with Raspberry Pi and examples_
- _2) HAT with Windows application_

## 1) Rainy UHF HAT with Raspberry Pi
 - For this connect HAT on Raspberry Pi and set jumper on HAT-UHF side as shown below. Also, make sure to connect suitable Antenna using SMA connector onboard.

   <img src="https://github.com/sbcshop/Rainy_UHF_HAT_Software/blob/main/images/RainUHFHAT_withPI.png" width="331" height="236">

 * Download and setup your Raspberry Pi with OS, you can follow the Getting Started [Link](https://www.raspberrypi.com/documentation/computers/getting-started.html) to perform OS installation.
 * You will have to enable Serial and SPI interface in Raspberry Pi, find instruction [here](https://github.com/sbcshop/Pitalk_4G_HAT_Software/blob/main/Documents/Serial%20Interface%20Enable%20RPi.pdf) 
 * Download complete github to Raspberry Pi,
   ```
   git clone https://github.com/sbcshop/Rainy_UHF_HAT_Software.git
   ```
    <img src="https://github.com/sbcshop/Rainy_UHF_HAT_Software/blob/main/images/git_download.jpg" width="490" height="90">

 * Open anyone [example](https://github.com/sbcshop/Rainy_UHF_HAT_Software/tree/main/examples) code in python IDE like IDLE, Thonny, etc. and run

    <img src="https://github.com/sbcshop/Rainy_UHF_HAT_Software/blob/main/images/run_examples.png" width="480" height="288">

    <img src="https://github.com/sbcshop/Rainy_UHF_HAT_Software/blob/main/images/output.png" width="480" height="288">

## 2) Rainy UHF HAT with Windows Application
  * You can use Rainy UHF HAT module directly with application. For this change jumper setting USB-UHF mode and connect hardware to laptop/PC using Type C as shown below.
    
    <img src="https://github.com/sbcshop/Rainy_UHF_HAT_Software/blob/main/images/RainyUHFHAT_withApp.png" width="" height="">
  
  * Now you can follow steps mentioned [here](https://github.com/sbcshop/Rainy_UHF_Breakout_Software#rainy-uhf-breakout-standalone) to use Rainy UHF module with standalone windows application.

## Resources
  * [Schematic](https://github.com/sbcshop/Rainy_UHF_HAT_Hardware/blob/main/Design%20Data/Rainy%20UHF%20HAT%20SCH.%20PDF.pdf)
  * [Hardware Files](https://github.com/sbcshop/Rainy_UHF_HAT_Hardware)
  * [Getting Started with Raspberry Pi](https://www.raspberrypi.com/documentation/computers/getting-started.html)
  * [Rainy UHF Module Command Manual](https://github.com/sbcshop/Rainy_UHF_Breakout_Software/blob/main/Document/Rainy%20UHF%20Module%20Command%20Manual.pdf)
  * [CH340 Driver Installation Guide](https://github.com/sbcshop/NFC_Module/blob/main/documents/CH340%20Driver%20installation%20steps.pdf)


## Related Products
  * [Rainy UHF Pico Expansion](https://shop.sb-components.co.uk/products/rainypi-uhf-based-on-pico-complete-kit) -  UHF Expansion board easily incorporate Pico/Pico W/Pico 2
  * [Rainy UHF for ESP32](https://shop.sb-components.co.uk/products/rainyfi-uhf-for-esp32-complete-board-kit) - UHF module with embedded ESP32 S3 for IoT prototyping.
  * [Rainy UHF SHIELD](https://shop.sb-components.co.uk/products/rainy-shield-for-arduino-board-complete-kit) - UHF Shield form factor for use with Arduino, Ardi-32, Ardi-Pi, and other compatible boards.
  * [Rainy UHF Breakout](https://shop.sb-components.co.uk/products/rainy-uhf-breakout-complete-kit) - Compact UHF module breakout with Type C for standalone use and TTL for interfacing with various MCU.

## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
