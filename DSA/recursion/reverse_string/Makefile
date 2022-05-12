# Toolchain path
#TCPATH = aarch64-linux-gnu-
TCPATH ?=

# Kernel Headers path
KERNELHEADERS = /usr/include/

CC := ${TCPATH}g++
CFLAGS = -Wall -g -lm

INCLUDES = -I$(KERNELHEADERS)

SOURCES = $(wildcard *.cpp)
OBJECTS := $(SOURCES:.cpp=.o)
EXEC = example

all: $(EXEC)

$(EXEC): $(OBJECTS)
	$(CC) $(CFLAGS) -o $(EXEC) $(OBJECTS)

.c.o:
	$(CC) -c $(CFLAGS) $(INCLUDES) -o $@ $<

clean:
	rm -f $(OBJECTS) $(EXEC)

install:

.PHONY: clean alls
