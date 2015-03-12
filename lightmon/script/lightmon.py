import spidev
 
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
 
# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts,places)
    return volts
 
# Define sensor channels
light_channel = 1
 
# Read the light sensor data
light_level = ReadChannel(light_channel)
light_volts = ConvertVolts(light_level,2)

# Print out results
print("Light: {} ({}V)".format(light_level,light_volts))