echo yes | python manage.py collectstatic
git add .
git commit -m "update static files"
git push origin main