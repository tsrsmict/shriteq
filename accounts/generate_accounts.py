import pathlib
import csv
import os

from accounts.models import School
from django.contrib.auth.models import User

base_path = pathlib.Path().resolve()

f = open(os.path.join(base_path, 'accounts', 'schools.csv'))
reader = csv.DictReader(f)
schools = list(reader)
f.close()

for school in schools:
    print(f'Creating school {school}')
    account_data = {'username': school['username'], 'password': school['password']}
    user = User.objects.create(**account_data)
    school_data = {'display_name': school['display_name'], 'account': user}
    School.objects.create(**school_data)