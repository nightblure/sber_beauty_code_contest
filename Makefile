run_flask_dev:
	flask --app src.flask_app:app run --port 5020 --debug --no-reload

run_flask:
	flask --app src.flask_app:app run --port 5020
