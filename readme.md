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
Pushes to the `origin/main` branch will automatically deploy the latest version of the main branch to the Heroku app. You can force a heroku deploy by running `git push heroku main`. 

# Reference articles
These articles and documentation pages were used for reference while configuring this project:
* [Medium tutorial on using Django + Tailwind + Heroku](https://medium.com/@phuitsing/heroku-buildpack-for-django-tailwind-de96be543f9)
* [Whitenoise config settings](http://whitenoise.evans.io/en/stable/django.html)
* [django-tailwind docs](https://django-tailwind.readthedocs.io/en/latest/installation.html)

# Commands
* `heroku logs --source app`: app-generated logs. Ignores Heroku-generated logs for every single GET request made to the server.

# Project structure
This section is meant for future users of this code, who may not have any experience at all with Django or Tailwind.

## Project and apps
Django is a batteries-included framework, meaning that the framework comes with a lot of tools and wrappers built in.

The first file you need to worry about is `manage.py`, in the root directory. You should never have to open it, but it's useful to know that this is the file that contains all the top-level commands for the application (for example, `runserver`).

A Django _project_ is what you're in right now. It has a root directory and within it a project folder which defines top-level configuration for the project. Here, that folder is `shriteq_website`. 
### Project folder
`settings.py` is where (self-explanatorily) you configure the project, and is loaded each time the server is run. Most of it is generated automatically on project creation. For a relatively simple app like this, you shouldn't need to mess around with it too much. 

Just note a few key things:
* The DEBUG setting defines whether the site should be in debug mode or production mode. In debug mode, it will give you error pages (and will generally be slower). Locally, this reads from a .env file. In Heroku, it would read from the Heroku Config vars (refer to Heroku documentation to find out how to set up config vars)
* The `ALLOWED_HOSTS` setting defines which URL the site is allowed to run on (to prevent HTTP Host header attacks). Django ignores this setting while DEBUG=True. When DEBUG=False, it will only run on URLs you allow it to run on. Make sure you set up all your Heroku and custom domains there.
* There's a piece of code which sets up a connection with Sentry, an error-tracking tool which logs errors in prod. Set up a sentry project (it's very easy!) and copy-paste their install code for Django.
* INSTALLED_APPS is a list of strings of 'app' names. Think of an app as a sub-module of functionality in the project. A bunch of apps come by default, some are third-party dependencies which inject functionality, and the others are defined by you.

`urls.py` in the `shriteq_website` folder (make sure you're looking at the right `urls.py` folder) is the entry point for URLs in your Django app. When your server receives a request, it looks up URLs starting from this file.This file defines `urlpatterns`, which is a list of routes on the app. 

Notice the `admin/` url comes by default - that's for the Django admin dashboard. Disregard the `__reload__/` path - that's only there to help you in development. The final line of the file adds your static URL - this is the URL from which static files are served (eg, `abc.com/static/main.css`).

The meat of `urls.py` is how it defines entry points for other apps - see `events.urls`. 
```path('', include('events.urls')),```
Here, we route any URL with that particular path (in this case, a blank beginning) onto the URLs defined in the `urls` file of the `events` app.
