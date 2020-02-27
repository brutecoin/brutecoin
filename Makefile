.PHONY: black flake8 isort lint typecheck help

help:
	@cat $(MAKEFILE_LIST)

black:
	pipenv run black .

flake8:
	pipenv run flake8 .

isort:
	pipenv run isort --recursive .

typecheck:
	pipenv run mypy .

lint: isort black flake8
