.PHONY: help clean format lint test install build update
.SILENT: help
.DEFAULT_GOAL := help

define PRINT_HELP_SCRIPT
import re, sys
for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_SCRIPT

help:
	@python -c "$$PRINT_HELP_SCRIPT" < $(MAKEFILE_LIST)

clean: ## remove all build, test and package artifacts
	rm -rf bin/
	go clean
	go mod tidy

format: ## format all source files
	go fmt
	go mod tidy

lint: ## check pre-commit linting rules
	pre-commit run --all-files --show-diff-on-failure --color always
	go vet

test: ## run tests quickly with the default Go
	go vet
	go test

install: clean ## install the package
	go install

build: clean ## build the package
	go build -o bin/

update: ## update all listed packages
	go get -u
	go mod tidy
