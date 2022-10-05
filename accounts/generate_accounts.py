import pathlib
import csv
import os
import random

from accounts.models import School
from django.contrib.auth.models import User

base_path = pathlib.Path().resolve()

f = open(os.path.join(base_path, 'accounts', 'schools.csv'))
reader = csv.DictReader(f)
schools = list(reader)
f.close()

# Shuffle schools so people don't whine about the crypt hunt
schools = sorted(schools, key=lambda i: i['display_name'])

for school in schools:
    print(f'Creating school {school}')
    user = User.objects.create_user(username = school['username'], password=school['password'])
    school_data = {'display_name': school['display_name'], 'account': user}
    School.objects.create(**school_data)