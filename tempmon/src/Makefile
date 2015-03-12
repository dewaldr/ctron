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

default: tempmon

tempmon: tempmon.o
	$(CC) $(LFLAGS) -o tempmon tempmon.o $(LIBS)

tempmon.o: tempmon.cpp
	$(CC) $(CCFLAGS) -o tempmon.o -c tempmon.cpp

clean:
	@rm -f tempmon *.o
	@rm -f *~

