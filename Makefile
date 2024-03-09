PYTHON ?= python

export PYTHONPATH := $(PWD)


version:
	@printf "Currently using executable: $(PYTHON)\n"
	which $(PYTHONE)
	$(PYTHON) --version

venv:
	[ -d .venv ] || $(PYTHON) -m venv .venv
	@printf ". .venv/Scripts/activate\n"
	@printf ". .venv/bin/activate\n"


install:
	$(PYTHON) -m pip install -r requirements.txt


installed:
	$(PYTHON) -m pip list


start:
	$(PYTHON) pig/main.py

clean:
	@$(call MESSAGE,$@)
	rm -f .coverage *.pyc
	rm -rf __pycache__
	rm -rf htmlcov

clean-doc: clean
	@$(call MESSAGE,$@)
	rm -rf doc

clean-all: clean clean-doc
	@$(call MESSAGE,$@)
	rm -rf .venv


pylint:
	@$(call MESSAGE,$@)
	-cd pig && $(PYTHON) -m pylint *.py


flake8:
	
	@$(call MESSAGE,$@)
	-flake8

lint: flake8 pylint



black:
	
	@$(call MESSAGE,$@)
	$(PYTHON) -m black pig/ test/


codestyle: black



unittest:
	
	@$(call MESSAGE,$@)
	$(PYTHON) -m unittest discover


coverage:

	@$(call MESSAGE,$@)
	coverage run -m unittest discover
	coverage html
	coverage report -m

test: lint coverage




pydoc:

	@$(call MESSAGE,$@)
	install -d doc/pydoc
	$(PYTHON) -m pydoc -w pig/*.py
	mv *.html doc/pydoc


pdoc:
	
	@$(call MESSAGE,$@)
	pdoc --force --html --output-dir doc/api pig/*.py


pyreverse:

	@$(call MESSAGE,$@)
	install -d doc/pyreverse
	pyreverse pig/*.py
	dot -Tpng classes.dot -o doc/pyreverse/classes.png
	dot -Tpng packages.dot -o doc/pyreverse/packages.png
	rm -f classes.dot packages.dot

doc: pdoc pyreverse #pydoc #sphinx


radon-cc:

	@$(call MESSAGE,$@)
	radon cc --show-complexity --average pig

radon-mi:

	@$(call MESSAGE,$@)
	radon mi --show pig

radon-raw:

	@$(call MESSAGE,$@)
	radon raw pig

radon-hal:

	@$(call MESSAGE,$@)
	radon hal pig

cohesion:

	@$(call MESSAGE,$@)
	cohesion --directory pig

metrics: radon-cc radon-mi radon-raw radon-hal cohesion


bandit:

	@$(call MESSAGE,$@)
	bandit --recursive pig

