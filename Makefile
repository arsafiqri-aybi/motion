.PHONY: verify labs search
verify:
	python3 scripts/validate.py
	python3 -m unittest discover -s tests -v
labs:
	python3 examples/run_labs.py --output .local-output/labs
search:
	python3 scripts/search.py "$(QUERY)"
