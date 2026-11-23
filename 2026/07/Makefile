.PHONY: help all run test tidy

help:
	@echo "make run   solve both parts against ./input"
	@echo "make test  check solve() against ./example and ./answer1, ./answer2"
	@echo "make tidy  format and lint-fix this day"
	@echo "make all   tidy, run, then test"

all: tidy run test

tidy:
	uv run ruff format .
	uv run ruff check --fix .

run:
	uv run python src/solve.py

test:
	uv run python -m unittest test.test
