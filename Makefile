PYTHON ?= python3

.PHONY: validate-registry

validate-registry:
	$(PYTHON) scripts/validate_registry.py
