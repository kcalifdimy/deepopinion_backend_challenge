# deepopinion_backend_challenge

This project is a DeepOpinion Challenge: Sr.


# Basic Commands

## Build Stack
docker-compose -f local.yml build

## Run the Stack 
docker-compose -f local.yml up

## Execute Management Commands
docker-compose -f local.yml run --rm django python manage.py migrate
docker-compose -f local.yml run --rm django python manage.py createsuperuser

## How to Use this Project
1. Run the build command 
2. Run the stack command to start the project
3. To upload CSV file, make post request to this endpoint: http://0.0.0.0:8000/api/v1/datas/upload-csv/ 
4. To upload Excel file, make post request to this endpoint: http://0.0.0.0:8000/api/v1/datas/upload-excel/ 
5. To get all data, make a get request to this endpoint: http://0.0.0.0:8000/api/v1/datas/data/
6. To get single data, make a get request to this endpoint: http://0.0.0.0:8000/api/v1/datas/data/{id}
7. To get all available sentiment, make a get rquest to the endpoint: http://0.0.0.0:8000/api/v1/datas/data/get_sentiment/
8. To get all available aspect, make a get rquest to the endpoint: http://0.0.0.0:8000/api/v1/datas/data/get_aspect/
9. Make sure the CSV and Excel file header name is Text, for data to be uploaded  

## What to Do
1. I was supposed to include download feature for CSV and Excel file 
2. I was supposed to add asynchronous task to all the request in the project but because of time i couldn't do that
3. I was supposed to write test cases for the programme but because of time I couldn't do it. 
4. I was supposed to cache end point that retrieve data from the database but due to time I couldn't do it. 

### Type checks

Running type checks with mypy:

    $ mypy deepopinion_backend_challenge

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

### Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at <https://sentry.io/signup/?code=cookiecutter> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

## Deployment

The following details how to deploy this application.

### Heroku

See detailed [cookiecutter-django Heroku documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html).

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
