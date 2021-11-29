# Makefile to handle setting up Python virtual environment
#
# Copyright (c) 2021 ZKM | Hertz-Lab
# Dan Wilcox <dan.wilcox@zkm.de>
#
# BSD Simplified License.
# For information on usage and redistribution, and for a DISCLAIMER OF ALL
# WARRANTIES, see the file, "LICENSE.txt," in this distribution.
#
# This code has been developed at ZKM | Hertz-Lab as part of „The Intelligent
# Museum“ generously funded by the German Federal Cultural Foundation.

VENV = venv
VBIN = $(VENV)/bin

PYTHON := python3
PIP := pip3

all: $(VENV)

.PHONY: clean

# set up python virtual environment and dependencies
$(VENV):
	$(PYTHON) -m venv "$(VENV)"
	$(VBIN)/$(PIP) install -r requirements.txt

# (re)generate a dependency requirements for current venv setup
freeze:
	$(VBIN)/$(PIP) freeze > requirements.txt

# force reinstall dendencies, useful after manually editing requirements.txt
reinstall:
	$(VBIN)/$(PIP) install --ignore-installed -r requirements.txt

# remove virtual environment
clean:
	rm -rf "$(VENV)"
