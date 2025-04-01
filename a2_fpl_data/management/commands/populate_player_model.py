import requests
from django.core.mail import send_mail
from django.conf import settings
import traceback
from django.core.management.base import BaseCommand
from a2_fpl_data.models import Player, Team, Region, Position

class Command(BaseCommand):
    help = "Fetches player data from the Bootstrap Static API and saves to the database"

    def handle(self, *args, **kwargs):

        try:
        
            URL = "https://fantasy.premierleague.com/api/bootstrap-static"

            players = requests.get(URL).json()['elements'] # send request to URL, put into JSON and filter just the 'teams' part
            
            for player in players:
                team_instance = Team.objects.get(team_id=player['team'])  # Get the Team instance
                position_instance = Position.objects.get(position_id=player['element_type'])  # Get the Team instance
                region_instance = None
                if player['region'] is not None:
                    try:
                        region_instance = Region.objects.get(region_id=player['region'])
                    except Region.DoesNotExist:
                        region_instance = None  # Set to None if the region is not found

                #self.stdout.write(player)

                _, created = Player.objects.update_or_create( 
                    player_id=player['id'], # Primary Key
                    defaults={
                        'team': team_instance,
                        'first_name': player['first_name'],
                        'second_name': player['second_name'],
                        'web_name': player['web_name'],
                        'photo': player['photo'],
                        'region': region_instance,
                        'birth_date': player['birth_date'],
                        'team_join_date': player['team_join_date'],
                        'position': position_instance
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Player {player['web_name']} - {player['id']} created"))  # Print if created
                else:
                    self.stdout.write(self.style.SUCCESS(f"Player {player['web_name']} - {player['id']} updated")) # Print if updated

        except Exception as e:

            error_message = f"An error occurred in the management command: {str(e)}\n"
            error_message += "Traceback:\n" + traceback.format_exc()

            send_mail(
            'Failed Management Command',
            'Your Player management command (populate_player_model.py) has failed.\n\n',
            error_message,
            settings.EMAIL_HOST_USER,
            [settings.ALERT_EMAIL_RECIPIENT],
            fail_silently=False,
        )