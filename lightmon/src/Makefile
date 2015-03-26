#
# Makefile for 'lightmon'.
#
# Type 'make' or 'make lightmon' to create the binary.
# Type 'make clean' to delete all temporaries.
#

# build target specs
CC      = g++
CCFLAGS = -fpermissive -Wall
LFLAGS  =
LIBS    = -lwiringPi

default: lightmon

lightmon: lightmon.o
	$(CC) $(LFLAGS) -o lightmon lightmon.o $(LIBS)

lightmon.o: lightmon.cpp
	$(CC) $(CCFLAGS) -o lightmon.o -c lightmon.cpp

clean:
	@rm -f lightmon *.o
	@rm -f *~

