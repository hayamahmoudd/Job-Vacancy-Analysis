# Makefile for Python scripts

# Define Python interpreter
PYTHON := python3

# Define the scripts
SCRIPTS := main.py question1.py question2.py question3.py

# Default target
.PHONY: all
all: run

# Run all scripts
.PHONY: run
run: $(SCRIPTS)
	@for script in $(SCRIPTS); do \
	    $(PYTHON) $$script; \
	done

# Run individual scripts
.PHONY: main question1 question2 question3
main:
	$(PYTHON) main.py 

question1:
	$(PYTHON) question1.py

question2:
	$(PYTHON) question2.py

question3:
	$(PYTHON) question3.py

# Clean up unnecessary files (e.g., compiled Python files)
.PHONY: clean
clean:
	@rm -f *.pyc */*.pyc __pycache__/*
