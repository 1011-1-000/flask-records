.PHONY: help test doc clean publish

.DEFAULT: help
help:
	@echo "make test"
	@echo "       run tests"
	@echo "make clean"
	@echo "       clean python cache files"
	@echo "make doc"
	@echo "       build sphinx documentation"
	@echo "make publish"
	@echo "       publish the lib to the pypi repository"


test: 
	python setup.py test

clean-pyc:
	@find . -name '*.pyc' -delete
	@find . -name '__pycache__' -type d | xargs rm -fr
	@find . -name '.pytest_cache' -type d | xargs rm -fr

clean-dist:
	@find . -name 'dist' -type d | xargs rm -fr
	@find . -name '*.egg-info' -type d | xargs rm -fr

clean-env:
	conda remove -

clean:clean-pyc clean-dist
	@echo "## Clean all data."

doc: 
	cd docs; make html

publish: 
	python setup.py publish