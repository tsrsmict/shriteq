# Todos

-[] Currently, variables for configuring the status of the crypt hunt and pac-man are in `settings.py`, which means that they get evaluated once after the application is booted, then not again. We need to rewrite these as _functions_ defined in a `utils.py` folder, and invole those functions every time the variables are currently referenced.
-[] Re-write crypt hunt to enable _media_ in questions as opposed to only supporting images and loading them as static files
-[] Rewrite events to pull from DB on homepage. This would allow us to have one description as a ground-truth for all event-related media, allow us to make changes without redeploying, and keep consistent values across the site without copy pasting. It would also enable event detail pages to require less manual HTML markup.

# Prerequisites

Make sure you have the following installed on your system:

- Python
- [Pipenv](https://pypi.org/project/pipenv/) (for Python dependency management - easier to use than standard `requirements.txt`)
- [NodeJS](https://github.com/nvm-sh/nvm)
- (optional, for deploy config) [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

# Tips

To run the accounts generation script:

1. SSH in
2. `python manage.py shell`
3. `exec(open('accounts/generate_accounts.py').read())`

## Development server

Run the following commands in your shell in the root directory of this repository:

1. `pipenv shell` (activates virtual environment)
2. `pipenv install` (install dependencies )
3. `python3 manage.py makemigrations` and `python3 manage.py migrate` (you won't need to run these every time, just the first time you're setting up the project and if you edit SQL model schema)
4. `python3 manage.py runserver`
   This will open the server on http://localhost:8000

## Tailwind

If you're editing the frontend with Tailwind CSS classes, you'll need to have the tailwind listener running

Steps:

1. Activate your pipenv: `pipenv shell`
2. Run `python3 manage.py tailwind start`. This will start a listener which automatically configures the tailwind files

Refer to the [django-tailwind docs](https://django-tailwind.readthedocs.io/en/latest/installation.html) for more instructions and debugging help on using Tailwind with Django in this project.

## Python dependencies

Install python dependencies with `pipenv install packagename` instead of `pip install packagename`. This will automatically add the package to the `Pipfile`, which is what we're using for dependency management.

# Reference articles

These articles and documentation pages were used for reference while configuring this project:

- [Medium tutorial on using Django + Tailwind + Heroku](https://medium.com/@phuitsing/heroku-buildpack-for-django-tailwind-de96be543f9)
- [Whitenoise config settings](http://whitenoise.evans.io/en/stable/django.html)
- [django-tailwind docs](https://django-tailwind.readthedocs.io/en/latest/installation.html)
