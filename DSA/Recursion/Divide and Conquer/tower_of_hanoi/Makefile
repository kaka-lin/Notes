# Toolchain path
TCPATH ?=

CC := ${TCPATH}gcc

SRCDIR = .
SOURCES = $(wildcard $(SRCDIR)/*.cc)
OBJECTS := $(SOURCES:.c=.o)
EXEC = hanoi

all: $(EXEC)

$(EXEC): $(OBJECTS)
	$(CC) -o $(EXEC) $(OBJECTS)

clean:
	rm -rf $(EXEC)

.PHONY: clean all
