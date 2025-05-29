from django.core.management.base import BaseCommand
from a4_analytics.models import PlayerDynamicData, PlayerDynamicDataRanks
from a2_fpl_data.models import Player, Gameweek
import sys

class Command(BaseCommand):
    # python3 manage.py populate_rank_model
    def handle(self, *args, **kwargs):
    
        current_gameweek = Gameweek.objects.get(is_current=True).gameweek
        player_list = PlayerDynamicData.objects.filter(gameweek=current_gameweek)

        sorted_dictionary = {
            "event_points": sorted(player_list, key=lambda x: x.event_points, reverse=True),
            "total_points": sorted(player_list, key=lambda x: x.total_points, reverse=True),
            "points_per_game": sorted(player_list, key=lambda x: x.points_per_game, reverse=True),
            "now_cost": sorted(player_list, key=lambda x: x.now_cost, reverse=True),
            "cost_change_event": sorted(player_list, key=lambda x: x.cost_change_event, reverse=True),
            "cost_change_start": sorted(player_list, key=lambda x: x.cost_change_start, reverse=True),
            "form": sorted(player_list, key=lambda x: x.form, reverse=True),
            "value_form": sorted(player_list, key=lambda x: x.value_form, reverse=True),
            "value_season": sorted(player_list, key=lambda x: x.value_season, reverse=True),
            "selected_by_percent": sorted(player_list, key=lambda x: x.selected_by_percent, reverse=True),
            "transfers_in_event": sorted(player_list, key=lambda x: x.transfers_in_event, reverse=True),
            "transfers_out_event": sorted(player_list, key=lambda x: x.transfers_out_event, reverse=True),
            "transfers_in": sorted(player_list, key=lambda x: x.transfers_in, reverse=True),
            "transfers_out": sorted(player_list, key=lambda x: x.transfers_out, reverse=True),
            "starts": sorted(player_list, key=lambda x: x.starts, reverse=True),
            "minutes": sorted(player_list, key=lambda x: x.minutes, reverse=True),
            "goals_scored": sorted(player_list, key=lambda x: x.goals_scored, reverse=True),
            'assists': sorted(player_list, key=lambda x: x.assists, reverse=True),
            "clean_sheets": sorted(player_list, key=lambda x: x.clean_sheets, reverse=True),
            "goals_conceded": sorted(player_list, key=lambda x: x.goals_conceded, reverse=True),
            "own_goals": sorted(player_list, key=lambda x: x.own_goals, reverse=True),
            "penalties_saved": sorted(player_list, key=lambda x: x.penalties_saved, reverse=True),
            "penalties_missed": sorted(player_list, key=lambda x: x.penalties_missed, reverse=True),
            "yellow_cards": sorted(player_list, key=lambda x: x.yellow_cards, reverse=True),
            "red_cards": sorted(player_list, key=lambda x: x.red_cards, reverse=True),
            "saves": sorted(player_list, key=lambda x: x.saves, reverse=True),
            "bonus": sorted(player_list, key=lambda x: x.bonus, reverse=True),
            "bps": sorted(player_list, key=lambda x: x.bps, reverse=True),
            "goals_conceded_per_90": sorted(player_list, key=lambda x: x.goals_conceded_per_90, reverse=True),
            "starts_per_90": sorted(player_list, key=lambda x: x.starts_per_90, reverse=True),
            "clean_sheets_per_90": sorted(player_list, key=lambda x: x.clean_sheets_per_90, reverse=True),
            "saves_per_90": sorted(player_list, key=lambda x: x.saves_per_90, reverse=True),
            "expected_goals": sorted(player_list, key=lambda x: x.expected_goals, reverse=True),
            "expected_assists": sorted(player_list, key=lambda x: x.expected_assists, reverse=True),
            "expected_goal_involvements": sorted(player_list, key=lambda x: x.expected_goal_involvements, reverse=True),
            "expected_goals_conceded": sorted(player_list, key=lambda x: x.expected_goals_conceded, reverse=True),
            "expected_goals_per_90": sorted(player_list, key=lambda x: x.expected_goals_per_90, reverse=True),
            "expected_assists_per_90": sorted(player_list, key=lambda x: x.expected_assists_per_90, reverse=True),
            "expected_goal_involvements_per_90": sorted(player_list, key=lambda x: x.expected_goal_involvements_per_90, reverse=True),
            "expected_goals_conceded_per_90": sorted(player_list, key=lambda x: x.expected_goals_conceded_per_90, reverse=True),
            "influence": sorted(player_list, key=lambda x: x.influence, reverse=True),
            "creativity": sorted(player_list, key=lambda x: x.creativity, reverse=True),
            "threat": sorted(player_list, key=lambda x: x.threat, reverse=True),
            "ict_index": sorted(player_list, key=lambda x: x.ict_index, reverse=True)
        }

        # Filter by position

        def filter_by_position(sorted_list, position):
            return [player for player in sorted_list if player.player.position.name_short == position]
        
        # Filter by team
        
        def filter_by_team(sorted_list, team):
            return [player for player in sorted_list if player.player.team.code == team]
        
        # Filter by position and team

        def filter_by_position_and_team(sorted_list, position, team):
            return [player for player in sorted_list if player.player.position.name_short == position and player.player.team.code == team]
        
        def create_json(player, stat, position, team):
            sorted_list = sorted_dictionary[stat]

            r1 = sorted_list.index(player) + 1 
            r2 = filter_by_position(sorted_list, position).index(player) + 1
            r3 = filter_by_team(sorted_list, team).index(player) + 1
            r4 = filter_by_position_and_team(sorted_list, position, team).index(player) + 1

            return {
                "all": r1,
                "pos": r2,
                "team": r3,
                "pos_team": r4
            }


        for player in player_list:

            created = False
            
            player_instance = Player.objects.get(player_id=player.player.player_id)  
            gameweek_instance = Gameweek.objects.get(gameweek=current_gameweek) 
            position = player.player.position.name_short
            team = player.player.team.code

            try:

                _, created = PlayerDynamicDataRanks.objects.update_or_create( 
                    player=player_instance,
                    defaults={
                        "gameweek": gameweek_instance,
                        "event_points" : create_json(player, "event_points", position, team),
                        "total_points": create_json(player, "total_points", position, team),
                        "points_per_game": create_json(player, "points_per_game", position, team),
                        "now_cost": create_json(player, "now_cost", position, team),
                        "cost_change_event": create_json(player, "cost_change_event", position, team),
                        "cost_change_start": create_json(player, "cost_change_start", position, team),
                        "form": create_json(player, "form", position, team),
                        "value_form": create_json(player, "value_form", position, team),
                        "value_season": create_json(player, "value_season", position, team),
                        "selected_by_percent": create_json(player, "selected_by_percent", position, team),
                        "transfers_in_event": create_json(player, "transfers_in_event", position, team),
                        "transfers_out_event": create_json(player, "transfers_out_event", position, team),
                        "transfers_in": create_json(player, "transfers_in", position, team),
                        "transfers_out": create_json(player, "transfers_out", position, team),
                        "starts": create_json(player, "starts", position, team),
                        "minutes": create_json(player, "minutes", position, team),
                        "goals_scored": create_json(player, "goals_scored", position, team),
                        'assists': create_json(player, "assists", position, team),
                        "clean_sheets": create_json(player, "clean_sheets", position, team),
                        "goals_conceded": create_json(player, "goals_conceded", position, team),
                        "own_goals": create_json(player, "own_goals", position, team),
                        "penalties_saved": create_json(player, "penalties_saved", position, team),
                        "penalties_missed": create_json(player, "penalties_missed", position, team),
                        "yellow_cards": create_json(player, "yellow_cards", position, team),
                        "red_cards": create_json(player, "red_cards", position, team),
                        "saves": create_json(player, "saves", position, team),
                        "bonus": create_json(player, "bonus", position, team),
                        "bps": create_json(player, "bps", position, team),
                        "goals_conceded_per_90": create_json(player, "goals_conceded_per_90", position, team),
                        "starts_per_90": create_json(player, "starts_per_90", position, team),
                        "clean_sheets_per_90": create_json(player, "clean_sheets_per_90", position, team),
                        "saves_per_90": create_json(player, "saves_per_90", position, team),
                        "expected_goals": create_json(player, "expected_goals", position, team),
                        "expected_assists": create_json(player, "expected_assists", position, team),
                        "expected_goal_involvements": create_json(player, "expected_goal_involvements", position, team),
                        "expected_goals_conceded": create_json(player, "expected_goals_conceded", position, team),
                        "expected_goals_per_90": create_json(player, "expected_goals_per_90", position, team),
                        "expected_assists_per_90": create_json(player, "expected_assists_per_90", position, team),
                        "expected_goal_involvements_per_90": create_json(player, "expected_goal_involvements_per_90", position, team),
                        "expected_goals_conceded_per_90": create_json(player, "expected_goals_conceded_per_90", position, team),
                        "influence": create_json(player, "influence", position, team),
                        "creativity": create_json(player, "creativity", position, team),
                        "threat": create_json(player, "threat", position, team),
                        "ict_index": create_json(player, "ict_index", position, team),
                    }
                )
            except Exception as f:
                print(f)

            if created:
                    self.stdout.write(self.style.SUCCESS(f"Player {player.player.web_name} - {player.player.player_id} created"))  # Print if created
            else:
                self.stdout.write(self.style.SUCCESS(f"Player {player.player.web_name} - {player.player.player_id} updated")) # Print if updated