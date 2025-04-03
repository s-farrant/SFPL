import requests
from django.core.management.base import BaseCommand
from a2_fpl_data.models import Fixture, Team, Player, Gameweek
import logging
import datetime

class Command(BaseCommand):
    help = "Fetches fixture data from the Fixture API and saves to the database"

    def handle(self, *args, **kwargs):
        run_log = logging.getLogger('mc_run')
        
        try:
        
            URL = "https://fantasy.premierleague.com/api/bootstrap-static"

            gameweeks = requests.get(URL).json()['events'] 

            for gameweek in gameweeks:

                created = False

                bboost_plays = None
                freehit_plays = None
                wildcard_plays = None
                triplec_plays = None
                manager_plays = None

                datetime_str = gameweek['deadline_time']
                datetime_str = datetime_str.rstrip('Z')
                date_str, time_str = datetime_str.split('T')

                if gameweek['finished'] == True:
                    player_instance_most_selected = Player.objects.get(player_id=gameweek['most_selected'])
                    player_instance_most_captained = Player.objects.get(player_id=gameweek['most_captained'])
                    player_instance_most_transferred_in = Player.objects.get(player_id=gameweek['most_transferred_in'])

                    for chip in gameweek['chip_plays']:
                        if chip['chip_name'] == "bboost":
                            bboost_plays = chip['num_played']
                        if chip['chip_name'] == "freehit":
                            freehit_plays = chip['num_played']
                        if chip['chip_name'] == "wildcard":
                            wildcard_plays = chip['num_played']
                        if chip['chip_name'] == "3xc":
                            triplec_plays = chip['num_played']
                        if chip['chip_name'] == "manager":
                            manager_plays = chip['num_played']
                else:
                    player_instance_most_selected = None
                    player_instance_most_captained = None
                    player_instance_most_transferred_in = None

                _, created = Gameweek.objects.update_or_create( 
                    gameweek=gameweek['id'], # Primary Key
                    defaults={
                        "start_date": date_str,
                        "start_time": time_str,
                        "average_score": gameweek['average_entry_score'],
                        "highest_score": gameweek['highest_score'],
                        "is_previous": gameweek['is_previous'],
                        "is_current": gameweek['is_current'],
                        "is_next": gameweek['is_next'],
                        "finished": gameweek['finished'],
                        "bboost_plays": bboost_plays,
                        "freehit_plays": freehit_plays,
                        "wildcard_plays": wildcard_plays,
                        "triplec_plays": triplec_plays,
                        "manager_plays": manager_plays,
                        "most_selected": player_instance_most_selected,
                        "most_captained": player_instance_most_captained,
                        "most_transferred_in": player_instance_most_transferred_in
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Gameweek {gameweek['id']} created"))  # Print if created
                else:
                    self.stdout.write(self.style.SUCCESS(f"Gameweek {gameweek['id']} updated")) # Print if updated

            run_log.info(f"POPULATE_GAMEWEEK: Ran successfully at {datetime.datetime.now()}") 


        except Exception as e:

            run_log.info(f"POPULATE_GAMEWEEK: Failed at {datetime.datetime.now()}") 
