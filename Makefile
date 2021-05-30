install:
	sudo python3 -m pip install -r requirements.txt
	sudo cp systemd/janitor.service /etc/systemd/system/
	sudo systemctl enable janitor && sudo systemctl start janitor

bootstrap:
	python3 src/janitor.py init_test

janitor-test:bootstrap
	python3 src/janitor.py arange_dir test/

start-janitor:
	python3 src/janitor.py janitor

start-janitor-cron:
	python3 src/janitor.py janitor_cron
