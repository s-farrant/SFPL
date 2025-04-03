import requests
from django.core.management.base import BaseCommand
from a2_fpl_data.models import Region
import logging
import datetime

class Command(BaseCommand):
    help = "Fetches region data from the Region API and saves to the database"

    def handle(self, *args, **kwargs):
        run_log = logging.getLogger('mc_run')

        try:
        
            URL = "https://fantasy.premierleague.com/api/regions"

            regions = requests.get(URL).json() 
            
            for region in regions:
                created = False

                _, created = Region.objects.update_or_create( 
                    region_id=region['id'],
                    defaults={
                        'name': region['name'],
                        'code': region['code'],
                        'iso_code_short': region['iso_code_short'],
                        'iso_code_long': region['iso_code_long']
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Region {region['name']} created")) # Print if created
                else:
                    self.stdout.write(self.style.SUCCESS(f"Region {region['name']} updated")) # Print if updated

            run_log.info(f"POPULATE_REGION: Ran successfully at {datetime.datetime.now()}")

        except Exception as e:

            run_log.info(f"POPULATE_REGION: Failed at {datetime.datetime.now()}")