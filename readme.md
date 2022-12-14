# Todos

### Critical

- [ ] Rewrite variables for checking open event status currently defined in `settings.py` as getter functions.

Currently, variables for configuring the status of the crypt hunt and pac-man are in `settings.py`, which means that they get evaluated once after the application is booted, then not again. We need to rewrite these as _functions_ defined in a `utils.py` folder, and invoke those functions every time the variables are currently referenced.

### Extremely useful

- [ ] Rewrite events to pull from DB on homepage. This would allow us to have one description as a ground-truth for all event-related media, allow us to make changes without redeploying, and keep consistent values across the site without copy pasting. It would also enable event detail pages to require less manual HTML markup.

### Nice to have

- [ ] Re-write crypt hunt to enable _media_ in questions as opposed to only supporting images and loading them as static files
- [ ] Rewrite banned IPs for crypt hunt and Pac-Man to be pulled from DB - won't need to update a text file and redeploy
- [ ] Unify player model for CH and Pac-Man, if continuing with Pac-Man in future years

# Prerequisites

Make sure you have the following installed on your system:

- Python
- [Pipenv](https://pypi.org/project/pipenv/) (for modern Python dependency management - easier to use than standard `requirements.txt` + `venv`)
- [NodeJS](https://github.com/nvm-sh/nvm) (for the TailwindCSS compiler - don't worry about this if you're just working on the backend)

# Tips

## Development server

Run the following commands in your shell in the root directory of this repository:

1. `pipenv shell` (activates virtual environment)
2. `pipenv install` (install dependencies )
3. `python3 manage.py makemigrations` and `python3 manage.py migrate` (you won't need to run these every time, just the first time you're setting up the project and if you edit SQL model schema)
4. `python3 manage.py runserver`
   This will open the server on http://localhost:8000

You must have a `.env` file with `SECRET_KEY` and `DEBUG` keys for this to work. Refer to the configuration in `settings.py` for more information on what format is expected.

## Tailwind

If you're editing the frontend with Tailwind CSS classes, you'll need to have the tailwind listener running

Steps:

1. Activate your pipenv: `pipenv shell`
2. Run `python3 manage.py tailwind start`. This will start a listener which automatically configures the tailwind files

Refer to the [django-tailwind docs](https://django-tailwind.readthedocs.io/en/latest/installation.html) for more instructions and debugging help on using Tailwind with Django in this project.

## Python dependencies

Install python dependencies with `pipenv install packagename` instead of `pip install packagename`. This will automatically add the package to the `Pipfile`, which is what we're using for dependency management.

## Misc.

To run the accounts generation script:

1. SSH in to the server
2. `python manage.py shell` to open the Django interactive Python terminal
3. `exec(open('accounts/generate_accounts.py').read())` - make sure you know what's in `generate_accounts.py`! This command will run whatever code is present in that file

# Reference articles

These articles and documentation pages were used for reference while configuring this project:

- [Medium tutorial on using Django + Tailwind + Heroku](https://medium.com/@phuitsing/heroku-buildpack-for-django-tailwind-de96be543f9)
- [Whitenoise config settings](http://whitenoise.evans.io/en/stable/django.html)
- [django-tailwind docs](https://django-tailwind.readthedocs.io/en/latest/installation.html)
