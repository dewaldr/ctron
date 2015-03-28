#!/bin/bash
#
# Usage:       cpumon
#
# Monitors CPU clock speed and temperature.
# 

cpu_freq=/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
cpu_temp=/sys/class/thermal/thermal_zone0/temp
if [ -e $cpu_freq ] ; then
    if [ -e $cpu_temp ] ; then
        clk=$(cat $cpu_freq)
        cpu=$(cat $cpu_temp)
        echo $(($clk/1000))"Mhz / "$(($cpu/1000))"°C" 
    fi
fi

