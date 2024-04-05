import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

import random

from AppTwo.models import Users

from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):

        fake_fn = fakegen.first_name()
        fake_ln = fakegen.last_name()
        fake_email = fakegen.email()

        user = Users.objects.get_or_create(first_name = fake_fn, last_name=fake_ln, email=fake_email)

if __name__ == '__main__':
    print("Creating data")
    populate(20)
    print("Finised populating")