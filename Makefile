CC=gcc-8
CXX=g++-8
CFLAGS=
CXXFLAGS=-rdynamic -g -O0 -std=c++17

DEPS=InlineClass.H InlineFunction.H
OBJS=RegularFunction.o RegularClass.o A.o B.o Main.o

.DEFAULT_GOAL := Main

%.o: %.C $(DEPS)
	$(CXX) -c -o $@ $< $(CXXFLAGS) # -M -MF $<.d

Main: $(OBJS)
	$(CXX) -o $@ $^ $(CXXFLAGS)

.PHONY: clean

clean:
	rm -rf *.o main
