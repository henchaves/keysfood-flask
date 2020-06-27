hello:
	echo "Hello"

clean:
	pip uninstall keysfood

install:
	pip install -e .['dev']

test:
	pytest tests/ -v