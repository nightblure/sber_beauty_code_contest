run_flask_dev:
	flask --app src.run_flask:app run --port 5020 --debug --reload

run_flask:
	flask --app src.run_flask:app run --host 0.0.0.0 --port 5020

build:
	docker-compose up -d
