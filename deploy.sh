echo yes | python manage.py collectstatic
git add .
git commit -m "update static files"
git push heroku main
heroku run python3 manage.py makemigrations
heroku run python3 manage.py migrate
heroku open
git push origin main