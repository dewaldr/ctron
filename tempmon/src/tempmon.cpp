#include <fstream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

int main()
{
    string token, line;
    string delimiter = "t=";
    size_t pos = 0;

    ifstream w1_file;
    w1_file.open("/sys/bus/w1/devices/28-0000059a0e02/w1_slave");

    if (w1_file.is_open()) {

        while (getline(w1_file, line)) {
            while ((pos = line.find(delimiter)) != string::npos) {
                token = line.substr(0, pos);
                line.erase(0, pos + delimiter.length());
                float value = roundf(atoi(line.c_str())) / 1000.0;
                printf("Temp: %.1f°C\n", value);
            }
        }

        w1_file.close();
    }
    else {
        printf("Error opening file\n");
    }

    return 0;
}



