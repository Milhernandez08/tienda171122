import os, django, random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "APIalmacen.settings")
django.setup()

from faker import Faker
from apps.products.models import Post
from django.contrib.auth.models import User

def create_post(N):
    fake = Faker()
    for _ in range(N):
        id += 1
        code = random.randint(1000, 9999)
        name = fake.name()
        description = fake.text()
        image = fake.title()

create_post(2)
print("Datos agregados")