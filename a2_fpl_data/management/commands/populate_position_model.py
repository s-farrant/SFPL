import requests
from django.core.management.base import BaseCommand
from a2_fpl_data.models import Position
import logging
import datetime

class Command(BaseCommand):
    help = "Fetches position data from the Bootstrap Static API and saves to the database"

    def handle(self, *args, **kwargs):
        run_log = logging.getLogger('mc_run')
        
        try:
        
            URL = "https://fantasy.premierleague.com/api/bootstrap-static"

            positions = requests.get(URL).json()['element_types']
            
            for position in positions:
                created = False
                
                _, created = Position.objects.update_or_create( 
                    position_id=position['id'], 
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

            run_log.info(f"POPULATE_POSITION: Ran successfully at {datetime.datetime.now()}")

        except Exception as e:

            run_log.info(f"POPULATE_POSITION: Failed at {datetime.datetime.now()}") 
