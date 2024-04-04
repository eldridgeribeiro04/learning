import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random

from first_app.models import AccessRecord, Webpage, Topic

from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        top = add_topic()

        fakeurl = fakegen.url()
        fakedate = fakegen.date()
        fakename = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic=top, name=fakename, url=fakeurl)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fakedate)[0]
        

if __name__ != '__main':
    print("Populating script")
    populate(N=20)
    print("Populating complete")