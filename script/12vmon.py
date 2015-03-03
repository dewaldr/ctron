import wiringpi2
import struct
import math

SPI_CHANNEL = 0
SPI_SPEED   = 1000000
FACTOR      = 80.2

wiringpi2.wiringPiSetup()

fd = wiringpi2.wiringPiSPISetup(SPI_CHANNEL, SPI_SPEED)
if fd < 0:
    print "Problem setting up SPI bus"
    exit(-1)

# Communicate with MCP3008 over SPI bus
# first byte: always 0b00000001
# second byte: single-ended on CH0 -> 0b10000000 : (SGL/DIFF=1, D2=D1=D0=0)
# third byte: always 0b00000000
data = struct.pack('BBB', 0b00000001, 0b10000000, 0b000000000)

ret = wiringpi2.wiringPiSPIDataRW(SPI_CHANNEL, data)

if ret < 0:
    print "Problem reading/writing on SPI bus"
    exit(-1)

a2d_result = struct.unpack('BBB', data)

a2d_value = 0
a2d_value = (a2d_result[1]<< 8) & 0b1100000000    # combine 10-bit return value, spread over bytes 1 and 2
a2d_value |= (a2d_result[2] & 0xff)

voltage = float(0)

# Use simple factor conversion, accurate at the top end of the scale
if a2d_value > 0:
    voltage = a2d_value / FACTOR

print "Measured voltage: ", format(voltage, '.1f'), "V"

