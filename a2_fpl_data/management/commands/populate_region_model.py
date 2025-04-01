import requests
from django.core.mail import send_mail
from django.conf import settings
import traceback
from django.core.management.base import BaseCommand
from a2_fpl_data.models import Region

class Command(BaseCommand):
    help = "Fetches region data from the Region API and saves to the database"

    def handle(self, *args, **kwargs):

        try:
        
            URL = "https://fantasy.premierleague.com/api/regions"

            regions = requests.get(URL).json() # send request to URL, put into JSON and filter just the 'teams' part
            
            for region in regions:
                _, created = Region.objects.update_or_create( 
                    region_id=region['id'], # Primary Key
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

        except Exception as e:

            error_message = f"An error occurred in the management command: {str(e)}\n"
            error_message += "Traceback:\n" + traceback.format_exc()

            send_mail(
            'Failed Management Command',
            'Your Region management command (populate_region_model.py) has failed.\n\n',
            error_message,
            settings.EMAIL_HOST_USER,
            [settings.ALERT_EMAIL_RECIPIENT],
            fail_silently=False,
        )