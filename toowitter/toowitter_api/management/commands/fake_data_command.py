from django.core.management.base import BaseCommand
from django.utils import timezone
import toowitter_api.fake_data_generator as fake_data_generator


class Command(BaseCommand):
    help = 'This will generate fake data and insert them to db for testing software.'

    def handle(self, *args, **kwargs):
        fake_data_generator.generate()
        self.stdout.write('Done.')
