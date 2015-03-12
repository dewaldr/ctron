#include <cstdlib>
#include <cerrno>
#include <cstdio>
#include <string>
#include <iostream>
#include <wiringPiSPI.h>

// The SPI bus speed seems to affect the ADC resolution
int speed = 1000000;
int channel = 1;
float max_scale = 1023;
float base_voltage = 3.3;

using namespace std;

int main(void)
{
    int a2dVal = 0;

    int fd = wiringPiSPISetup (channel, speed);
    if (fd < 0){
        perror("Problem setting up SPI");
        exit(1);
    }

    unsigned char data[3];
    data[0] = 1;  //  first byte transmitted -> start bit
    //data[1] = 0b10000000 |(((channel & 7) << 4)); // second byte transmitted -> (SGL/DIF = 1, D2=D1=D0=0)
    data[1] = (8 + channel) << 4;
    data[2] = 0; // third byte transmitted....don't care


    int ret = wiringPiSPIDataRW(channel, data, sizeof(data));
    cout << "SPI R/W returned: " << ret << endl;

    a2dVal = 0;
    a2dVal = (data[1]<< 8) & 0b1100000000; //merge data[1] & data[2] to get result
    a2dVal |=  (data[2] & 0xff);

    cout << "ADC recorded: " << a2dVal << endl;

    float voltage = 0;

    // Use simple factor conversion, accurate at the top end of the scale
    if (a2dVal > 0) {
        voltage = (a2dVal * base_voltage) / max_scale;
    }

    cout << fixed;
    cout.precision(1);
    cout << voltage << "V" << endl;

    return 0;
}
