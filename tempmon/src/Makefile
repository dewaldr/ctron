#
# Makefile for 'tempmon'.
#
# Type 'make' or 'make tempmon' to create the binary.
# Type 'make clean' to delete all temporaries.
#

# build target specs
CC      = g++
CCFLAGS = -O2 -Wall
LFLAGS  =
LIBS    =

default: tempmon list-1w-sensors

tempmon: tempmon.o
	$(CC) $(LFLAGS) -o tempmon tempmon.o $(LIBS)

tempmon.o: tempmon.cpp
	$(CC) $(CCFLAGS) -o tempmon.o -c tempmon.cpp

list-1w-sensors: list-1w-sensors.o
	$(CC) $(LFLAGS) -o list-1w-sensors list-1w-sensors.o $(LIBS)

list-1w-sensors.o: list-1w-sensors.cpp
	$(CC) $(CCFLAGS) -o list-1w-sensors.o -c list-1w-sensors.cpp

clean:
	@rm -f tempmon list-1w-sensors *.o
	@rm -f *~

