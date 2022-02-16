from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create admin user'

    def add_arguments(self, parser):
        parser.add_argument('--username', required=True, type=str)
        parser.add_argument('--password', required=True, type=str)

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']

        if User.objects.filter(username=username).exists():
            print('Superuser creation skipped.')
        else:
            User.objects.create_superuser(username, '', password)
            print('Superuser created.')
