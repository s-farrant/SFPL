import requests
from django.core.mail import send_mail
from django.conf import settings
import traceback
from django.core.management.base import BaseCommand
from a2_fpl_data.models import Position

class Command(BaseCommand):
    help = "Fetches position data from the Bootstrap Static API and saves to the database"

    def handle(self, *args, **kwargs):

        try:
        
            URL = "https://fantasy.premierleague.com/api/bootstrap-static"

            positions = requests.get(URL).json()['element_types'] # send request to URL, put into JSON and filter just the 'teams' part
            
            for position in positions:

                _, created = Position.objects.update_or_create( 
                    position_id=position['id'], # Primary Key
                    defaults={
                        'name_long': position['singular_name'],
                        'name_short': position['singular_name_short'],
                        'squad_select': position['squad_select'],
                        'squad_min_play': position['squad_min_play'],
                        'squad_max_play': position['squad_max_play']
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Position {position['singular_name']} created"))  # Print if created
                else:
                    self.stdout.write(self.style.SUCCESS(f"Player {position['singular_name']} updated")) # Print if updated

        except Exception as e:

            error_message = f"An error occurred in the management command: {str(e)}\n"
            error_message += "Traceback:\n" + traceback.format_exc()

            send_mail(
            'Failed Management Command',
            'Your Position management command (populate_position_model.py) has failed.\n\n',
            error_message,
            settings.EMAIL_HOST_USER,
            [settings.ALERT_EMAIL_RECIPIENT],
            fail_silently=False,
        )