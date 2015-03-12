#
# Makefile for '12vmon'.
#
# Type 'make' or 'make 12vmon' to create the binary.
# Type 'make clean' to delete all temporaries.
#

# build target specs
CC      = g++
CCFLAGS = -O2 -Wall
LFLAGS  =
LIBS    = -lwiringPi

default: 12vmon

12vmon: 12vmon.o
	$(CC) $(LFLAGS) -o 12vmon 12vmon.o $(LIBS)

12vmon.o: 12vmon.cpp
	$(CC) $(CCFLAGS) -o 12vmon.o -c 12vmon.cpp

clean:
	@rm -f 12vmon *.o
	@rm -f *~

