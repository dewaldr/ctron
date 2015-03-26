#include <fstream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <glob.h>
#include <string>
#include <vector>
#include "tclap/CmdLine.h"

using namespace TCLAP;
using namespace std;

bool _verbose;
string _device;

void parseOptions(int argc, char** argv);

vector<string> get_sensors(const string& pattern){
    glob_t glob_result;
    glob(pattern.c_str(),GLOB_TILDE,NULL,&glob_result);
    vector<string> files;
    for(unsigned int i=0;i<glob_result.gl_pathc;++i){
        files.push_back(string(glob_result.gl_pathv[i]));
    }
    globfree(&glob_result);

    return files;
}

int main(int argc, char* argv[])
{
    parseOptions(argc,argv);

    string pattern = "/sys/bus/w1/devices/28-*";
    vector<string> sensors = get_sensors(pattern);

    for (vector<string>::iterator it = sensors.begin(); it != sensors.end(); ++it) 
    {
        string token, line;
        string delimiter = "t=";
        size_t pos = 0;

        ifstream w1_file;

        string filename;
        filename += (*it);
        filename += "/w1_slave";

        if ( _verbose == true ) printf("Opening device file: %s\n", filename.c_str());

        w1_file.open(filename.c_str());

        if (w1_file.is_open()) {
    
            if ( _verbose == true ) printf("Querying device...\n");

            while (getline(w1_file, line)) {

                if ( _verbose == true ) printf("Parsing line: %s\n", line.c_str());

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
            return -1;
        }
    }

    return 0;
}


void parseOptions(int argc, char* argv[])
{
    try {
        // Define the command line object.
        CmdLine cmd("Dallas Semiconductor 18B20 temperature sensor", ' ', "0.1");

        // Verbose flag
        SwitchArg verboseArg( "v", "verbose", "Print additional information", false );
        cmd.add( verboseArg );

        // Verbose flag
        ValueArg<string>  deviceArg("d","device","Device ID to read",true, "28-xxxxx", "Device");
        cmd.add( deviceArg );

        // Parse the args.
        cmd.parse( argc, argv );

        // Get the value parsed by each arg.
        _verbose = verboseArg.getValue();

    }
    catch ( ArgException& e) {
        printf("error: %s for arg %s\n", (e.error()).c_str(), (e.argId()).c_str());
    }
}


