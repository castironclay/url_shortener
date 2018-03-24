from django.core.management.base import BaseCommand, CommandError

from shortener.models import ClayURL

class Command(BaseCommand):
    help = 'Refreshes all ClayURL shortcodes'

    #arguments
    def add_arguments(self, parser):
        # no longer a required argument
        # must be an integer
        argument = parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return ClayURL.objects.refresh_shortcodes(items=options['items'])
