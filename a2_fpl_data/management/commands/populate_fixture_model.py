import requests
from django.core.management.base import BaseCommand
from a2_fpl_data.models import Fixture, Team
import logging
import datetime

class Command(BaseCommand):
    help = "Fetches fixture data from the Fixture API and saves to the database"

    def handle(self, *args, **kwargs):
        run_log = logging.getLogger('mc_run')
        
        try:
        
            URL = "https://fantasy.premierleague.com/api/fixtures"

            fixtures = requests.get(URL).json()

            for fixture in fixtures:
                created = False

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

            run_log.info(f"POPULATE_FIXTURE: Ran successfully at {datetime.datetime.now()}") 

        except Exception as e:

            run_log.info(f"POPULATE_FIXTURE: Failed at {datetime.datetime.now()}")