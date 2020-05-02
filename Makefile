CF_PWD = `pwd`

.PHONY: test
test:
	pytest --junitxml=junit/test-results.xml --cov=cashflow --cov-report=xml --cov-report=html --cov-fail-under=100 ; \
	echo "Coverage report available at ${CF_PWD}/htmlcov/index.html"