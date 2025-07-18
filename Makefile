#Variables
PYTHON_INTERPRETER=python 
PIP=pip 
SHELL=/bin/bash
PYTHONPATH=$(pwd) #TODO: check this should it be $(shell pwd)

#venv
create-environment: 
	@echo "creating venv..."
	$(PYTHON_INTERPRETER) -m venv venv
	@echo "venv created"

set-pythonpath: 
	export PYTHONPATH=$(PYTHONPATH)

activate-venv: #TODO: will this work without pythonpath first?? 
	@echo "Activating venv"
	source venv/bin/activate
	@echo "venv activated"


#install 
install-requirements: 
	@echo "installing requirements..."
	source venv/bin/activate && $(PIP) install -r ./requirements.txt 
	@echo "Requirements installed"

install-dev-tools: 
	@echo "installing dev tools"
	source venv/bin/activate && $(PIP) install bandit black safety flake 8 
#TODO: check these out 

unit-test: 
	source venv/bin/activate && $(PYTHONPATH) pytest -vvvrp 
#TODO: 

#security 
security-check: 
	source venv/bin/activate && safety check -r ./requirements.txt
	source venv/bin/activate && bandit -lll */*.py *c/*.pytest
#TODO: check this out 

#compliance... #TODO: what to add here? 

set-up: create-environment set-pythonpath activate-venv
installation: install-requirements install-dev-tools unit-test


#TODO: finalise makefile and complete Github actions CI/CD .yml 