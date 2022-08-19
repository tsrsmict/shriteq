To run the local server, make sure you have the following installed:
* Python
* Pipenv
* (optional, for deploy debugging) Heroku CLI

Instructions:
1. `pipenv shell`
2. `pipenv install`
3. `python3 manage.py makemigrations`
4. `python3 manage.py migrate`
5. `python3 manage.py runserver`
This will open the server on localhost:8000
