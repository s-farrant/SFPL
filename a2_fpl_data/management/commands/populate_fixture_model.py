import requests
from django.core.mail import send_mail
from django.conf import settings
import traceback
from django.core.management.base import BaseCommand
from a2_fpl_data.models import Fixture, Team

class Command(BaseCommand):
    help = "Fetches fixture data from the Fixture API and saves to the database"

    def handle(self, *args, **kwargs):

        try:
        
            URL = "https://fantasy.premierleague.com/api/fixtures"

            fixtures = requests.get(URL).json()
            
            for fixture in fixtures:

                team_a_instance = Team.objects.get(team_id=fixture['team_a']) 
                team_h_instance = Team.objects.get(team_id=fixture['team_h']) 

                if fixture['kickoff_time'] != None:
                    datetime_str = fixture['kickoff_time']
                    datetime_str = datetime_str.rstrip('Z')
                    date_str, time_str = datetime_str.split('T')


                    _, created = Fixture.objects.update_or_create( 
                        fixture_id=fixture['id'],
                        defaults={
                            'code': fixture['code'],
                            'pulse_id': fixture['pulse_id'],
                            'event': fixture['event'],
                            'finished': fixture['finished'],
                            'kickoff_date': date_str,
                            'kickoff_time': time_str,
                            'team_a': team_a_instance,
                            'team_h': team_h_instance,
                            'team_a_score': fixture['team_a_score'],
                            'team_h_score': fixture['team_h_score']
                        }
                    )

                    if created:
                        self.stdout.write(self.style.SUCCESS(f"Fixture {fixture['id']} created"))  # Print if created
                    else:
                        self.stdout.write(self.style.SUCCESS(f"Fixture {fixture['id']} updated")) # Print if updated
                else:
                    pass
        
        except Exception as e:

            error_message = f"An error occurred in the management command: {str(e)}\n"
            error_message += "Traceback:\n" + traceback.format_exc()

            send_mail(
            'Failed Management Command',
            'Your Fixture management command (populate_fixture_model.py) has failed.\n\n',
            error_message,
            settings.EMAIL_HOST_USER,
            [settings.ALERT_EMAIL_RECIPIENT],
            fail_silently=False,
        )