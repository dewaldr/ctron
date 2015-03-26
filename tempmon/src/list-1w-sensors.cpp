#include <glob.h>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

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

int main(void)
{
    string pattern = "/sys/bus/w1/devices/28-*";
    vector<string> sensors = get_sensors(pattern);

    for (vector<string>::iterator it = sensors.begin(); it != sensors.end(); ++it) {
        cout << *it << endl;
    }

    return 0;
}
