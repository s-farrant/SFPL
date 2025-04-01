import requests
from django.core.mail import send_mail
from django.conf import settings
import traceback
from django.core.management.base import BaseCommand
from a2_fpl_data.models import Team

class Command(BaseCommand):
    help = "Fetches teams data from the Bootstrap Static API and saves to the database"

    def handle(self, *args, **kwargs):

        try:
        
            URL = "https://fantasy.premierleague.com/api/bootstrap-static"

            teams = requests.get(URL).json()['teams'] # send request to URL, put into JSON and filter just the 'teams' part
            
            for team in teams:
                _, created = Team.objects.update_or_create( 
                    code=team['code'], # Primary Key
                    defaults={
                        'team_id': team['id'],
                        'team_name': team['name'],
                        'short_name': team['short_name'],
                        'logo_url': None,
                        'strength_overall_home': team['strength_overall_home'],
                        'strength_overall_away': team['strength_overall_away'],
                        'strength_attack_home': team['strength_attack_home'],
                        'strength_attack_away': team['strength_attack_away'],
                        'strength_defence_home': team['strength_defence_home'],
                        'strength_defence_away': team['strength_defence_away']
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Team {team['name']} created")) # Print if created
                else:
                    self.stdout.write(self.style.SUCCESS(f"Team {team['name']} updated")) # Print if updated

        except Exception as e:

            error_message = f"An error occurred in the management command: {str(e)}\n"
            error_message += "Traceback:\n" + traceback.format_exc()

            send_mail(
            'Failed Management Command',
            'Your Team management command (populate_team_model.py) has failed.\n\n',
            error_message,
            settings.EMAIL_HOST_USER,
            [settings.ALERT_EMAIL_RECIPIENT],
            fail_silently=False,
        )