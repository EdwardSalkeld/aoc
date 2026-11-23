.PHONY: help tidy test

DAYS := $(sort $(wildcard [0-9][0-9]))

help:
	@echo "make tidy  format and lint-fix every day"
	@echo "make test  run every day's example tests"

tidy:
	uv run ruff format .
	uv run ruff check --fix .

test:
	@for d in $(DAYS); do echo "== $$d"; $(MAKE) -s -C $$d test || exit 1; done
