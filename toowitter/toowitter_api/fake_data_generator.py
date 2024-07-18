from faker import Faker
from .models import *


def generate():
    for i in range(0, 5 + 1):
        fake = Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()
        domain_name = fake.domain_name()
        email = f"{first_name}{last_name}@{domain_name}"
        user = User(email=email, username=fake.user_name(
        ), name=f"{first_name} {last_name}", bio=fake.text(max_nb_chars=128), password=fake.password())

        user.save()

        for i in range(0, 25):
            Tweet(text=fake.sentence(), user=user, ).save()
