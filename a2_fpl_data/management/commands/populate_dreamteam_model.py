import requests
from django.core.mail import send_mail
from django.conf import settings
import traceback
from django.core.management.base import BaseCommand
from a2_fpl_data.models import Dreamteam, Player, Gameweek
import sys

class Command(BaseCommand):
    help = "Fetches dreamteam data from the dreamteam API and saves to the database"

    def handle(self, *args, **kwargs):

        try:
        
            URL = "https://fantasy.premierleague.com/api/dream-team/{gameweek_id}"

            for gameweek in range(1,38):
                dreamteam = requests.get(URL.format(gameweek_id=str(gameweek))).json()

                if 'team' in dreamteam:
                    length = 0
                    for i in range(0, len(dreamteam['team'])):
                        player_instance = Player.objects.get(player_id=dreamteam['team'][i]['element'])
                        gameweek_instance = Gameweek.objects.get(gameweek=gameweek)

                        _, created = Dreamteam.objects.update_or_create( 
                            gameweek= gameweek_instance,
                            player= player_instance,
                            defaults={
                                'points': dreamteam['team'][i]['points']
                            }
                        )
                        length = length+1
                else:
                    sys.exit()

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Dreamteam gameweek {gameweek} created, {length} instances"))  # Print if created
                else:
                    self.stdout.write(self.style.SUCCESS(f"Dreamteam gameweek {gameweek} updated, {length} instances")) # Print if updated
        
        except Exception as e:

            error_message = f"An error occurred in the management command: {str(e)}\n"
            error_message += "Traceback:\n" + traceback.format_exc()

            send_mail(
            'Failed Management Command',
            'Your Dreamteam management command (populate_dreamteam_model.py) has failed.\n\n',
            error_message,
            settings.EMAIL_HOST_USER,
            [settings.ALERT_EMAIL_RECIPIENT],
            fail_silently=False,
        )