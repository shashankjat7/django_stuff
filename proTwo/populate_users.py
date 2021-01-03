import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','proTwo.settings')

import django
django.setup()

## fake pop script
import random
from users.models import user
from faker import Faker

fakegen=Faker()

def populate(N=5):
    for i in range(N):
        fake_name = fakegen.name()
        fake_age = random.randint(0,100)
        fake_email = fakegen.email()

        user_detail = user.objects.get_or_create(name=fake_name,age=fake_age,email=fake_email)[0]
        user_detail.save()


if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('populating complete!')
    