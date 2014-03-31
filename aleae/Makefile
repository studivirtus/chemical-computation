# ----------------------------------------------------------------------------
# file			  | Makefile 
# project		  | Probabilistic Analysis of Biochemical Reactions (Bio Ludo Aleae)
# author(s)		  | Marc Riedel 
# affiliation(s) | Electrical and Computer Engineering, University of Minnesota
# created		  | 2006/02/08
# modified		  | 2006/02/08
# copyright		  | University of Minnesota (c) 2006
# ----------------------------------------------------------------------------

# directories

ALEAE_HOME		= "./"

# ----------------------------------------------------------------------------
# compiler, libraries, includes, flags

CC					= g++
LIBS				= -lm
INCLUDEDIRS		= -I$(ALEAE_HOME)
CFLAGS			= -O3 $(INCLUDEDIRS)
CFLAGS-g			= -g -Wall $(INCLUDEDIRS)
CFLAGS-pg		= -pg -Wall $(INCLUDEDIRS)
CPPFLAGS			= $(CFLAGS)

# ----------------------------------------------------------------------------
# virtual path

VPATH				= $(ALEAE_HOME)

# ----------------------------------------------------------------------------
# object files

ALEAE_HDRS		= aleae.h 
ALEAE_OBJS		= aleae_io.o		  \
					  aleae_main.o		  \
					  aleae_stoch.o	  

# -----------------------------------------------------------------------------
# default target

all: aleae

# -----------------------------------------------------------------------------
# build programs

# aleae

$(ALEAE_OBJS): $(ALEAE_HDRS) 

aleae: $(ALEAE_OBJS) 
	$(CC) $(CFLAGS) $(ALEAE_OBJS) -o $@

aleae-g: 
	${MAKE} 'CFLAGS=$(CFLAGS-g)' aleae

aleae-pg: 
	${MAKE} 'CFLAGS=$(CFLAGS-pg)' aleae

# -----------------------------------------------------------------------------
# clean

clean: 
	rm -f *.o 
