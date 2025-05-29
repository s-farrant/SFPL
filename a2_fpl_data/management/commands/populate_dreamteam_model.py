import requests
from django.core.management.base import BaseCommand
from a2_fpl_data.models import Dreamteam, Player, Gameweek
import sys
import logging
import datetime

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        run_log = logging.getLogger('mc_run')

        try:

            current_gameweek_instance = Gameweek.objects.get(is_current=True)
            gameweek = current_gameweek_instance.gameweek

            Dreamteam.objects.filter(gameweek=gameweek).delete()

            for week in range(1,gameweek+1):

                URL = "https://fantasy.premierleague.com/api/dream-team/{gameweek_id}"
                
                dreamteam = requests.get(URL.format(gameweek_id=str(week))).json()

                if 'team' in dreamteam:
                    length = 0
                    for i in range(0, len(dreamteam['team'])):
                        created = False
                        player_instance = Player.objects.get(player_id=dreamteam['team'][i]['element'])
                        gameweek_instance = Gameweek.objects.get(gameweek=week)

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
                    self.stdout.write(self.style.SUCCESS(f"Dreamteam gameweek {week} created, {length} instances"))  # Print if created
                else:
                    self.stdout.write(self.style.SUCCESS(f"Dreamteam gameweek {week} updated, {length} instances")) # Print if updated
            

            run_log.info(f"POPULATE_DREAMTEAM: Ran successfully at {datetime.datetime.now()}")
        
        except Exception as e:
  
            run_log.info(f"POPULATE_DREAMTEAM: Failed at {datetime.datetime.now()}")
    