bootstrap:
	python3 src/janitor.py init_test

janitor-test:bootstrap
	python3 src/janitor.py arange_dir test/

start-janitor:
	python3 src/janitor.py janitor 
