import requests
from django.core.management.base import BaseCommand
from a2_fpl_data.models import Player, Team, Region, Position
import logging
import datetime

class Command(BaseCommand):
    help = "Fetches player data from the Bootstrap Static API and saves to the database"

    def handle(self, *args, **kwargs):
        run_log = logging.getLogger('mc_run')
        
        try:
        
            URL = "https://fantasy.premierleague.com/api/bootstrap-static"

            players = requests.get(URL).json()['elements'] 
            
            for player in players:
                created = False
                team_instance = Team.objects.get(team_id=player['team'])  
                position_instance = Position.objects.get(position_id=player['element_type'])  
                region_instance = None
                if player['region'] is not None:
                    try:
                        region_instance = Region.objects.get(region_id=player['region']) # populate_player_model
                    except Region.DoesNotExist:
                        region_instance = None 

                _, created = Player.objects.update_or_create( 
                    player_id=player['id'], 
                    defaults={
                        'team': team_instance,
                        'first_name': player['first_name'],
                        'second_name': player['second_name'],
                        'web_name': player['web_name'],
                        'squad_number': player['squad_number'],
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
            
            print(f"POPULATE_PLAYER: Ran successfully at {datetime.datetime.now()}") 

        except Exception as e:
            print(e)
            print(f"POPULATE_PLAYER: Failed at {datetime.datetime.now()}") 
