# 12vmon
## Another Raspberry Pi 12V battery monitor

This project provides another take on adding an Analogue to Digital Converter (ADC) to the Raspberry Pi, by using an MCP3008 to monitor a 12V battry supply level, and reading the result over the Serial Periperal Interface (SPI) bus.

My design is based heavilyon that of Hussam Al-Hertani, over at https://github.com/halherta/RaspberryPi-mcp3008Spi.

## Hardware
The ADC is an inexpensive MCP3008 IC, which provides up to 8 analogue channels. However, the Raspberry Pi SPI kernel implementation only allows 2 channels to be read. The MCP3008 operates on 3.3V, therefore 12V input signal has to be attenuated using a simple voltage divider. I chose 2.2kOhm and 750Ohm for my values of R1 and R2 respectively. As I expect the battery to output voltages exceeding 13V, this provides a small margin for error. See breadboard schematic attached. The remaining connections hook up the MCP3008 to the SPI bus on the Raspberry Pi. These are the Clock Signal, Data In, Data Out and Slave Select.

## Software
I used halherta's Mcp3008Spi class, with a minor bugfix, to interface to the MCP3008. The newer RasPi firmware has a reworked SPI kernel module that produced an 'Invalid argument' ioctl error. A simple memset to clear the SPI buffer before populating it fixes this issue.
