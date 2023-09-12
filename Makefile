run_flask_dev:
	flask --app src.run_flask:app run --port 5020 --debug --reload

run_flask:
	flask --app src.run_flask:app run --port 5020
