from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
import logging
import datetime
import traceback
from django.conf import settings
from django.core.mail import send_mail

class Command(BaseCommand):

    def handle(self, *args, **options):
        run_log = logging.getLogger('mc_run')

        commands = [
            "populate_team_model",
            "populate_gameweek_model",
            "populate_fixture_model",
            "populate_dreamteam_model",
            "populate_dynamic_model"
        ]

        for command in commands:
            try:
                call_command(*command.split())
                run_log.info(f"SUCCESS - Run All - ({command}): Successful at {datetime.datetime.now()}")
            except Exception as e:
            
                run_log.info(f"FAIL - Run Necessary - ({command}): Failed at {datetime.datetime.now()}. With: {e}")
