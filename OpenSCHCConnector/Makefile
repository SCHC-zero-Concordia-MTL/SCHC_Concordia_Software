VENV=venv
PYTHON_PATH=$(VENV)/bin/python3
PIP_PATH=$(VENV)/bin/pip3
APP_NAME=connector
.PHONY: all init clean install run

all: init install run

init:
	@if [ -d $(VENV) ]; then \
		echo "A python virtual environment already exists."; \
	else \
		echo "Creating a python virtual environment" && python3 -m venv $(VENV); \
	fi

clean:
	@if [ -d $(VENV) ]; then \
		rm -r $(VENV); \
	else \
		echo "There is nothing to clean in the project directory"; \
	fi

install:
	@echo "Installing the required python libraries"
	$(PIP_PATH) install -r requirements.txt

run:
	$(PYTHON_PATH) $(APP_NAME).py