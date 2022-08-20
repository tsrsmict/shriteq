# Prerequisites
Make sure you have the following installed on your system:
* Python
* [Pipenv](https://pypi.org/project/pipenv/)
* [NodeJS](https://github.com/nvm-sh/nvm)
* (optional, for deploy config) [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

# Development
## Development server
Run the following commands in your shell in the root directory of this repository:
1. `pipenv shell` (activates virtual environment)
2. `pipenv install` (install dependencies )
3. `python3 manage.py makemigrations` and `python3 manage.py migrate` (you won't need to run these every time, just the first time you're setting up the project and if you edit SQL model schema)
5. `python3 manage.py runserver`
This will open the server on http://localhost:8000

## Tailwind
If you're editing the frontend with Tailwind CSS classes, you'll need to have the tailwind listener running
Steps:
1. Activate your pipenv: `pipenv shell`
2. Run `python3 manage.py tailwind start`. This will start a listener which automatically configures the tailwind files

Refer to the [django-tailwind docs](https://django-tailwind.readthedocs.io/en/latest/installation.html) for more instructions and debugging help on using Tailwind with Django in this project.

## Python dependencies
Install python dependencies with `pipenv install packagename` instead of `pip install packagename`. This will automatically add the package to the `Pipfile`, which is what we're using for dependency management.

# Deploys
Pushes to the `origin/main` branch will automatically deploy the latest version of the main branch to the Heroku app. Use `deploy.sh` as a deploy script, which should collect static files and push to the origin branch.

You can force a heroku deploy by running `git push heroku main`. 

# Reference articles
These articles and documentation pages were used for reference while configuring this project:
* [Medium tutorial on using Django + Tailwind + Heroku](https://medium.com/@phuitsing/heroku-buildpack-for-django-tailwind-de96be543f9)
* [Whitenoise config settings](http://whitenoise.evans.io/en/stable/django.html)
* [django-tailwind docs](https://django-tailwind.readthedocs.io/en/latest/installation.html)