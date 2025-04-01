import requests
from django.core.mail import send_mail
from django.conf import settings
import traceback
from django.core.management.base import BaseCommand
from a2_fpl_data.models import Player, Gameweek
from a4_analytics.models import PlayerDynamicData

class Command(BaseCommand):
    help = "Fetches player data from the Bootstrap Static API and saves to the database"

    def handle(self, *args, **kwargs):

        try:
        
            URL = "https://fantasy.premierleague.com/api/bootstrap-static"

            bootstrap = requests.get(URL).json()

            players = bootstrap['elements'] # send request to URL, put into JSON and filter just the 'teams' part

            for gameweek in bootstrap['events']:
                if gameweek['is_current'] == True:
                    gameweek_current = gameweek['id']
            
            for player in players:
                player_instance = Player.objects.get(player_id=player['id'])  # Get the Team instance
                gameweek_instance = Gameweek.objects.get(gameweek=gameweek_current)  # Get the Team instance

                _, created = PlayerDynamicData.objects.update_or_create( 
                    player=player_instance, # Primary Key
                    defaults={
                        "gameweek": gameweek_instance,
                        "event_points" : player['event_points'],
                        "total_points" : player['total_points'],
                        "ep_next" : float(player['ep_next']),
                        "points_per_game" : player['points_per_game'],

                        "now_cost" : player['now_cost'],
                        "cost_change_event" : player['cost_change_event'],
                        "cost_change_start" : player['cost_change_start'],
                        "form" : player['form'],
                        "value_form" : player['value_form'],
                        "value_season" : player['value_season'],

                        "selected_by_percent" : player['selected_by_percent'],
                        "transfers_in_event" : player['transfers_in_event'],
                        "transfers_out_event" : player['transfers_out_event'],
                        "transfers_in" : player['transfers_in'],
                        "transfers_out" : player['transfers_out'],

                        "status" : player['status'],

                        "starts" : player['starts'],
                        "minutes" : player['minutes'],
                        "goals_scored" : player['goals_scored'],
                        "assists" : player['assists'],
                        "clean_sheets" : player['clean_sheets'],
                        "goals_conceded" : player['goals_conceded'],
                        "own_goals" : player['own_goals'],
                        "penalties_saved" : player['penalties_saved'],
                        "penalties_missed" : player['penalties_missed'],
                        "yellow_cards" : player['yellow_cards'],
                        "red_cards" : player['red_cards'],
                        "saves" : player['saves'],
                        "bonus" : player['bonus'],
                        "bps" : player['bps'],
                        "goals_conceded_per_90" : player['goals_conceded_per_90'],
                        "starts_per_90" : player['starts_per_90'],
                        "clean_sheets_per_90" : player['clean_sheets_per_90'],
                        "saves_per_90" : player['saves_per_90'],

                        "expected_goals" : player['expected_goals'],
                        "expected_assists" : player['expected_assists'],
                        "expected_goal_involvements" : player['expected_goal_involvements'],
                        "expected_goals_conceded" : player['expected_goals_conceded'],
                        "expected_goals_per_90" : player['expected_goals_per_90'],
                        "expected_assists_per_90" : player['expected_assists_per_90'],
                        "expected_goal_involvements_per_90" : player['expected_goal_involvements_per_90'],
                        "expected_goals_conceded_per_90" : player['expected_goals_conceded_per_90'],

                        "influence" : player['influence'],
                        "creativity" : player['creativity'],
                        "threat" : player['threat'],
                        "ict_index" : player['ict_index'],

                        "influence_rank" : player['influence_rank'],
                        "influence_rank_type" : player['influence_rank_type'],
                        "creativity_rank" : player['creativity_rank'],
                        "creativity_rank_type" : player['creativity_rank_type'],
                        "threat_rank" : player['threat_rank'],
                        "threat_rank_type" : player['threat_rank_type'],
                        "ict_index_rank" : player['ict_index_rank'],
                        "ict_index_rank_type" : player['ict_index_rank_type'],

                        "now_cost_rank" : player['now_cost_rank'],
                        "now_cost_rank_type" : player['now_cost_rank_type'],
                        "form_rank" : player['form_rank'],
                        "form_rank_type" : player['form_rank_type'],
                        "points_per_game_rank" : player['points_per_game_rank'],
                        "points_per_game_rank_type" : player['points_per_game_rank_type'],
                        "selected_rank" : player['selected_rank'],
                        "selected_rank_type" : player['selected_rank_type']

                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Player {player['web_name']} - {player['id']} created"))  # Print if created
                else:
                    self.stdout.write(self.style.SUCCESS(f"Player {player['web_name']} - {player['id']} updated")) # Print if updated

        except Exception as e:

            error_message = f"An error occurred in the management command: {str(e)}\n"
            error_message += "Traceback:\n" + traceback.format_exc()

            send_mail(
            'Failed Management Command',
            'Your Player Dynamic Data management command (populate_dynamic_model.py) has failed.\n\n',
            error_message,
            settings.EMAIL_HOST_USER,
            [settings.ALERT_EMAIL_RECIPIENT],
            fail_silently=False,
        )