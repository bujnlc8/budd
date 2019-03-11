build:
	python setup.py bdist_wheel --universal

install:
	pip install dist/*.whl

test:
	python -m tests.__init__