import logging
from django.shortcuts import render
from a2_fpl_data.models import Player, Team, Gameweek
from .models import PlayerDynamicData, PlayerDynamicDataRanks
from django.views import View
from pprint import pprint
from django.db.models import Q

logger = logging.getLogger(__name__)

# Creating the Context structure

def create_context(model, stat_fields):

    current_gameweek = Gameweek.objects.get(is_current=True)

    player_details = model.objects.filter(gameweek=current_gameweek)

    position_ids = {
        'gkp': 1,
        'def': 2,
        'mid': 3,
        'fwd': 4
    }

    def build_player_list(players):
        return [
            {
                "player": p.player,
                "team": p.player.team,
                "stats": {field: getattr(p, field) for field in stat_fields}
            }
            for p in players
            if p.player.position.name_short != "MNG"
        ]
    
    all_players = build_player_list(player_details)

    position_lists = {
        pos: build_player_list(player_details.filter(gameweek=current_gameweek, player__position__position_id=pos_id))
        for pos, pos_id in position_ids.items()
    }

    def sort_by_stat(players, stat):
        return sorted(players, key=lambda x: x['stats'][stat], reverse=True)

    context = {
        "stat_lists": {},
        "stat_keys": stat_fields
    }

    for stat in stat_fields:
        context['stat_lists'][stat] = {}
        context['stat_lists'][stat]['all'] = sort_by_stat(all_players, stat)

    for pos, players in position_lists.items():
        for stat in stat_fields:
            context['stat_lists'][stat][pos] = sort_by_stat(players, stat)

    return context

# Format text

def process_dict_percent(context):
    for key, value in context.items():
        
        if isinstance(value, dict):
            process_dict_percent(value)
        
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict) and 'stats' in item and 'selected_by_percent' in item['stats']:
                    selected_by_percent = item['stats']['selected_by_percent']
                    if isinstance(selected_by_percent, (int, float)):
                        item['stats']['selected_by_percent'] = str(selected_by_percent) + "%"
                    else:
                        break
    return context

def process_dict_number_format(context):
    for key, value in context.items():
        
        if isinstance(value, dict):
            process_dict_number_format(value)
        
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict) and 'stats' in item and 'transfers_in' in item['stats']:
                    transfers_in = item['stats']['transfers_in']
                    transfers_in_event = item['stats']['transfers_in_event']
                    transfers_out = item['stats']['transfers_out']
                    transfers_out_event = item['stats']['transfers_out_event']
                    if isinstance(transfers_in, (int, float)):
                        item['stats']['transfers_in'] = f"{transfers_in:,}"
                        item['stats']['transfers_in_event'] = f"{transfers_in_event:,}"
                        item['stats']['transfers_out'] = f"{transfers_out:,}"
                        item['stats']['transfers_out_event'] = f"{transfers_out_event:,}"
                    else:
                        break
    return context

def process_dict_cost(context):
    for key, value in context.items():
        
        if isinstance(value, dict):
            process_dict_cost(value)
        
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict) and 'stats' in item and 'now_cost' in item['stats']:
                    now_cost = item['stats']['now_cost']
                    if isinstance(now_cost, (int, float)):
                        item['stats']['now_cost'] = f"£{now_cost:.2f}"[:-1]+ "m"
                    else:
                        break
    return context

# ICT

class ICT(View):
    def get(self, request):
        context = create_context(
            PlayerDynamicData, 
            stat_fields=["influence", "creativity", "threat", "ict_index"]
            )
        return render(request, 'a4_analytics/ict.html', context)
    

# Player value

class PlayerValue(View):
    def get(self, request):
        context = create_context(
            PlayerDynamicData, 
            stat_fields=["total_points", "points_per_game", "now_cost", "form", "value_season", "value_form"]
            )

        context = process_dict_cost(context)

        return render(request, 'a4_analytics/player-value.html', context)
    
# In-game

class InGame(View):
    def get(self, request):
        context = create_context(
            PlayerDynamicData, 
            stat_fields=["goals_scored", "assists", "clean_sheets", "bonus", "expected_goals", "expected_assists", "expected_goal_involvements", "expected_goals_conceded", "expected_goals_per_90", "expected_assists_per_90", "expected_goal_involvements_per_90"]
            )
        
        return render(request, 'a4_analytics/in-game.html', context)


# Transfers   

class Transfers(View):
    def get(self, request):
        context = create_context(
            PlayerDynamicData, 
            stat_fields=["cost_change_start", "cost_change_event", "selected_by_percent", "transfers_in", "transfers_in_event", "transfers_out", "transfers_out_event"]
            )
        
        context = process_dict_percent(context)
        context = process_dict_number_format(context)

        return render(request, 'a4_analytics/transfers.html', context)