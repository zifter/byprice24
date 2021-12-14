from crawler.tasks import get_agent
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Schedule scarping for '

    def add_arguments(self, parser):
        parser.add_argument('--force', action='store_true', default=False)

    def handle(self, *args, **options):
        force = options.get('force', False)
        get_agent().schedule(force=force)
