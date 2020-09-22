.PHONY: test migrate-dev make-migrations-dev runserver-dev

runserver-dev: 
	python manage.py runserver --settings=config.settings.local


make-migrations-dev:
	python manage.py makemigrations --settings=config.settings.local

migrate-dev: 
	python manage.py migrate --settings=config.settings.local

test:
	coverage run -m pytest -s --durations=0 .
	coverage report
	coverage html
