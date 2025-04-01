import logging
from django.shortcuts import render
from a2_fpl_data.models import Player, Team, Gameweek
from .models import PlayerDynamicData
from django.views import View
from django.db.models import Q

logger = logging.getLogger(__name__)

# ICT

class ICT(View):
    def get(self, request):
        
        current_gameweek = Gameweek.objects.get(is_current=True)

        player_details = PlayerDynamicData.objects.filter(gameweek=current_gameweek)


        player_details_gkp = PlayerDynamicData.objects.filter(
            Q(gameweek=current_gameweek) & Q(player__position__position_id=1))
        
        player_details_def = PlayerDynamicData.objects.filter(
            Q(gameweek=current_gameweek) & Q(player__position__position_id=2))
        
        player_details_mid = PlayerDynamicData.objects.filter(
            Q(gameweek=current_gameweek) & Q(player__position__position_id=3))
        
        player_details_fwd = PlayerDynamicData.objects.filter(
            Q(gameweek=current_gameweek) & Q(player__position__position_id=4))
    

        player_list = []
        player_list_gkp = []
        player_list_def = []
        player_list_mid = []
        player_list_fwd = []

        # all

        for player in player_details:
            player_list.append({
                "player": player.player,
                "team": player.player.team,
                "ict_stats": {
                    "influence": player.influence,
                    "influence_rank": player.influence_rank,
                    "influence_rank_type": player.influence_rank_type,
                    "creativity": player.creativity,
                    "creativity_rank": player.creativity_rank,
                    "creativity_rank_type": player.creativity_rank_type,
                    "threat": player.threat,
                    "threat_rank": player.threat_rank,
                    "threat_rank_type": player.threat_rank_type,
                    "ict_index": player.ict_index,
                    "ict_index_rank": player.ict_index_rank,
                    "ict_index_rank_type": player.ict_index_rank_type
                }
            })

        # gkp
        
        for player in player_details_gkp:
            player_list_gkp.append({
                "player": player.player,
                "team": player.player.team,
                "ict_stats": {
                    "influence": player.influence,
                    "influence_rank": player.influence_rank,
                    "influence_rank_type": player.influence_rank_type,
                    "creativity": player.creativity,
                    "creativity_rank": player.creativity_rank,
                    "creativity_rank_type": player.creativity_rank_type,
                    "threat": player.threat,
                    "threat_rank": player.threat_rank,
                    "threat_rank_type": player.threat_rank_type,
                    "ict_index": player.ict_index,
                    "ict_index_rank": player.ict_index_rank,
                    "ict_index_rank_type": player.ict_index_rank_type
                }
            })

        # def

        for player in player_details_def:
            player_list_def.append({
                "player": player.player,
                "team": player.player.team,
                "ict_stats": {
                    "influence": player.influence,
                    "influence_rank": player.influence_rank,
                    "influence_rank_type": player.influence_rank_type,
                    "creativity": player.creativity,
                    "creativity_rank": player.creativity_rank,
                    "creativity_rank_type": player.creativity_rank_type,
                    "threat": player.threat,
                    "threat_rank": player.threat_rank,
                    "threat_rank_type": player.threat_rank_type,
                    "ict_index": player.ict_index,
                    "ict_index_rank": player.ict_index_rank,
                    "ict_index_rank_type": player.ict_index_rank_type
                }
            })

        # mid

        for player in player_details_mid:
            player_list_mid.append({
                "player": player.player,
                "team": player.player.team,
                "ict_stats": {
                    "influence": player.influence,
                    "influence_rank": player.influence_rank,
                    "influence_rank_type": player.influence_rank_type,
                    "creativity": player.creativity,
                    "creativity_rank": player.creativity_rank,
                    "creativity_rank_type": player.creativity_rank_type,
                    "threat": player.threat,
                    "threat_rank": player.threat_rank,
                    "threat_rank_type": player.threat_rank_type,
                    "ict_index": player.ict_index,
                    "ict_index_rank": player.ict_index_rank,
                    "ict_index_rank_type": player.ict_index_rank_type
                }
            })

        # fwd

        for player in player_details_fwd:
            player_list_fwd.append({
                "player": player.player,
                "team": player.player.team,
                "ict_stats": {
                    "influence": player.influence,
                    "influence_rank": player.influence_rank,
                    "influence_rank_type": player.influence_rank_type,
                    "creativity": player.creativity,
                    "creativity_rank": player.creativity_rank,
                    "creativity_rank_type": player.creativity_rank_type,
                    "threat": player.threat,
                    "threat_rank": player.threat_rank,
                    "threat_rank_type": player.threat_rank_type,
                    "ict_index": player.ict_index,
                    "ict_index_rank": player.ict_index_rank,
                    "ict_index_rank_type": player.ict_index_rank_type
                }
            })

        sorted_influence = sorted(player_list, key=lambda x: x['ict_stats']['influence'], reverse=True)
        sorted_creativity = sorted(player_list, key=lambda x: x['ict_stats']['creativity'], reverse=True)
        sorted_threat = sorted(player_list, key=lambda x: x['ict_stats']['threat'], reverse=True)
        sorted_ict_index = sorted(player_list, key=lambda x: x['ict_stats']['ict_index'], reverse=True)

        sorted_influence_gkp = sorted(player_list_gkp, key=lambda x: x['ict_stats']['influence'], reverse=True)
        sorted_creativity_gkp = sorted(player_list_gkp, key=lambda x: x['ict_stats']['creativity'], reverse=True)
        sorted_threat_gkp = sorted(player_list_gkp, key=lambda x: x['ict_stats']['threat'], reverse=True)
        sorted_ict_index_gkp = sorted(player_list_gkp, key=lambda x: x['ict_stats']['ict_index'], reverse=True)

        sorted_influence_def = sorted(player_list_def, key=lambda x: x['ict_stats']['influence'], reverse=True)
        sorted_creativity_def = sorted(player_list_def, key=lambda x: x['ict_stats']['creativity'], reverse=True)
        sorted_threat_def = sorted(player_list_def, key=lambda x: x['ict_stats']['threat'], reverse=True)
        sorted_ict_index_def = sorted(player_list_def, key=lambda x: x['ict_stats']['ict_index'], reverse=True)

        sorted_influence_mid = sorted(player_list_mid, key=lambda x: x['ict_stats']['influence'], reverse=True)
        sorted_creativity_mid = sorted(player_list_mid, key=lambda x: x['ict_stats']['creativity'], reverse=True)
        sorted_threat_mid = sorted(player_list_mid, key=lambda x: x['ict_stats']['threat'], reverse=True)
        sorted_ict_index_mid = sorted(player_list_mid, key=lambda x: x['ict_stats']['ict_index'], reverse=True)

        sorted_influence_fwd = sorted(player_list_fwd, key=lambda x: x['ict_stats']['influence'], reverse=True)
        sorted_creativity_fwd = sorted(player_list_fwd, key=lambda x: x['ict_stats']['creativity'], reverse=True)
        sorted_threat_fwd = sorted(player_list_fwd, key=lambda x: x['ict_stats']['threat'], reverse=True)
        sorted_ict_index_fwd = sorted(player_list_fwd, key=lambda x: x['ict_stats']['ict_index'], reverse=True)

        context = {
            "sorted_influence": sorted_influence,
            "sorted_creativity": sorted_creativity,
            "sorted_threat": sorted_threat,
            "sorted_ict": sorted_ict_index,

            "sorted_influence_gkp": sorted_influence_gkp,
            "sorted_creativity_gkp": sorted_creativity_gkp,
            "sorted_threat_gkp": sorted_threat_gkp,
            "sorted_ict_gkp": sorted_ict_index_gkp,

            "sorted_influence_def": sorted_influence_def,
            "sorted_creativity_def": sorted_creativity_def,
            "sorted_threat_def": sorted_threat_def,
            "sorted_ict_def": sorted_ict_index_def,

            "sorted_influence_mid": sorted_influence_mid,
            "sorted_creativity_mid": sorted_creativity_mid,
            "sorted_threat_mid": sorted_threat_mid,
            "sorted_ict_mid": sorted_ict_index_mid,

            "sorted_influence_fwd": sorted_influence_fwd,
            "sorted_creativity_fwd": sorted_creativity_fwd,
            "sorted_threat_fwd": sorted_threat_fwd,
            "sorted_ict_fwd": sorted_ict_index_fwd
        }
    
        return render(request, 'a4_analytics/ict.html', context)
    

# In-game

class InGameStats(View):
    def get(self, request):
        
        current_gameweek = Gameweek.objects.get(is_current=True)

        player_details = PlayerDynamicData.objects.filter(gameweek=current_gameweek)

        player_list = []

        for player in player_details:
            player_list.append({
                "player": player.player,
                "team": player.player.team,
                "in_game_stats": {
                    "goals_scored": 1,
                    "assists": 1,
                    "clean_sheets": 1,
                    "bonus": 1,
                    "expected_goals": 1,
                    "expected_assists": 1,
                    "expected_goal_involvements": 1,
                    "expected_goals_conceded": 1,
                    "expected_goals_per_90": 1,
                    "expected_assists_per_90": 1,
                    "expected_goal_involvements_per_90": 1,
                    "expected_goals_conceded_per_90": 1
                }
            })

        sorted_influence = sorted(player_list, key=lambda x: x['ict_stats']['influence'], reverse=True)
        sorted_creativity = sorted(player_list, key=lambda x: x['ict_stats']['creativity'], reverse=True)
        sorted_threat = sorted(player_list, key=lambda x: x['ict_stats']['threat'], reverse=True)
        sorted_ict_index = sorted(player_list, key=lambda x: x['ict_stats']['ict_index'], reverse=True)

        context = {
            "sorted_influence": sorted_influence,
            "sorted_creativity": sorted_creativity,
            "sorted_threat": sorted_threat,
            "sorted_ict": sorted_ict_index
        }
    
        return render(request, 'a4_analytics/in-game.html', context)
    
# Transfers

class Transfers(View):
    def get(self, request):
        
        current_gameweek = Gameweek.objects.get(is_current=True)

        player_details = PlayerDynamicData.objects.filter(gameweek=current_gameweek)

        player_list = []

        for player in player_details:
            player_list.append({
                "player": player.player,
                "team": player.player.team,
                "ict_stats": {
                    "influence": player.influence,
                    "influence_rank": player.influence_rank,
                    "influence_rank_type": player.influence_rank_type,
                    "creativity": player.creativity,
                    "creativity_rank": player.creativity_rank,
                    "creativity_rank_type": player.creativity_rank_type,
                    "threat": player.threat,
                    "threat_rank": player.threat_rank,
                    "threat_rank_type": player.threat_rank_type,
                    "ict_index": player.ict_index,
                    "ict_index_rank": player.ict_index_rank,
                    "ict_index_rank_type": player.ict_index_rank_type
                }
            })

        sorted_influence = sorted(player_list, key=lambda x: x['ict_stats']['influence'], reverse=True)
        sorted_creativity = sorted(player_list, key=lambda x: x['ict_stats']['creativity'], reverse=True)
        sorted_threat = sorted(player_list, key=lambda x: x['ict_stats']['threat'], reverse=True)
        sorted_ict_index = sorted(player_list, key=lambda x: x['ict_stats']['ict_index'], reverse=True)

        context = {
            "sorted_influence": sorted_influence,
            "sorted_creativity": sorted_creativity,
            "sorted_threat": sorted_threat,
            "sorted_ict": sorted_ict_index
        }
    
        return render(request, 'a4_analytics/transfers.html', context)
    

# Player value

class PlayerValue(View):
    def get(self, request):
        
        current_gameweek = Gameweek.objects.get(is_current=True)

        player_details = PlayerDynamicData.objects.filter(gameweek=current_gameweek)

        player_list = []

        for player in player_details:
            player_list.append({
                "player": player.player,
                "team": player.player.team,
                "ict_stats": {
                    "influence": player.influence,
                    "influence_rank": player.influence_rank,
                    "influence_rank_type": player.influence_rank_type,
                    "creativity": player.creativity,
                    "creativity_rank": player.creativity_rank,
                    "creativity_rank_type": player.creativity_rank_type,
                    "threat": player.threat,
                    "threat_rank": player.threat_rank,
                    "threat_rank_type": player.threat_rank_type,
                    "ict_index": player.ict_index,
                    "ict_index_rank": player.ict_index_rank,
                    "ict_index_rank_type": player.ict_index_rank_type
                }
            })

        sorted_influence = sorted(player_list, key=lambda x: x['ict_stats']['influence'], reverse=True)
        sorted_creativity = sorted(player_list, key=lambda x: x['ict_stats']['creativity'], reverse=True)
        sorted_threat = sorted(player_list, key=lambda x: x['ict_stats']['threat'], reverse=True)
        sorted_ict_index = sorted(player_list, key=lambda x: x['ict_stats']['ict_index'], reverse=True)

        context = {
            "sorted_influence": sorted_influence,
            "sorted_creativity": sorted_creativity,
            "sorted_threat": sorted_threat,
            "sorted_ict": sorted_ict_index
        }
    
        return render(request, 'a4_analytics/player-value.html', context)
