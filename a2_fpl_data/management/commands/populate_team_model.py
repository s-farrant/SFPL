import requests
from django.core.management.base import BaseCommand
from a2_fpl_data.models import Team
import logging
import datetime

class Command(BaseCommand):
    help = "Fetches teams data from the Bootstrap Static API and saves to the database"

    def handle(self, *args, **kwargs):
        run_log = logging.getLogger('mc_run')

        try:
        
            URL = "https://fantasy.premierleague.com/api/bootstrap-static"

            teams = requests.get(URL).json()['teams']
            
            for team in teams:
                created = False
                
                _, created = Team.objects.update_or_create( 
                    code=team['code'], 
                    defaults={
                        'team_id': team['id'],
                        'team_name': team['name'],
                        'short_name': team['short_name'],
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
            
            run_log.info(f"POPULATE_TEAM: Ran successfully at {datetime.datetime.now()}")

        except Exception as e:

            run_log.info(f"POPULATE_TEAM: Failed at {datetime.datetime.now()}")