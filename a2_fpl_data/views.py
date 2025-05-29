from django.shortcuts import render
from collections import Counter
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import ListView
from django.views import View
from django.urls import reverse_lazy
import requests
from django.shortcuts import render
from .models import Team, Region, Player, Fixture, Position, Dreamteam, Gameweek
from a4_analytics.models import PlayerDynamicData, PlayerDynamicDataRanks
from django.http import JsonResponse
import logging
from django.db.models import Window, F
from django.db.models.functions import Rank
from django.db.models import Q
from pprint import pprint

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

# Create your views here.

class DreamteamView(View):
    def get(self, request, gameweek):
        dreamteam_players = Dreamteam.objects.filter(gameweek=gameweek)

        past_dreamteams = Dreamteam.objects.filter(gameweek__lte=gameweek)
        player_counts = Counter(past_dreamteams.values_list("player__player_id", flat=True))

        gameweeks = Dreamteam.objects.values('gameweek').distinct()
        
        available_gameweeks = [gw['gameweek'] for gw in gameweeks]
        available_gameweeks.sort()
        
        gk = []
        df = []
        mf = []
        fw = []

        total = 0

        for dreamteam_entry in dreamteam_players:
            player = dreamteam_entry.player
            position = player.position
            team = player.team

            player_data ={
                'player': player,
                'points': dreamteam_entry.points,
                'team': team,
                'position': position.name_short if position else "N/A",
                'dreamteam_count': player_counts.get(player.player_id, 0)
            }

            if position.name_short == "GKP":
                gk.append(player_data)
            elif position.name_short == "DEF":
                df.append(player_data)
            elif position.name_short == "MID":
                mf.append(player_data)
            elif position.name_short == "FWD":
                fw.append(player_data)
            
            total = total + dreamteam_entry.points

        context = {
            'selected_gameweek': gameweek,
            'gkp': gk,
            'def': df,
            'mid': mf,
            'fwd': fw,
            'total': total,
            'available_gameweeks': available_gameweeks
        }

        
        return render(request, 'a2_fpl_data/dreamteam.html', context)
    
class TOTS(View):

    def get(self, request):

        gameweeks = Dreamteam.objects.values('gameweek').distinct()
        
        available_gameweeks = [gw['gameweek'] for gw in gameweeks]

        current_gameweek = Gameweek.objects.get(is_current=True)

        player_details = PlayerDynamicData.objects.filter(gameweek=current_gameweek)  

        sorted_players = sorted([{
            "player": p.player, 
            "team": p.player.team, 
            "points": p.total_points} 
        for p in player_details],
        key=lambda x: x['points'],
        reverse=True
        )

        gk = [[p for p in sorted_players if p['player'].position.name_short == 'GKP'][0]]
        df = [p for p in sorted_players if p['player'].position.name_short == 'DEF'][0:5]
        md = [p for p in sorted_players if p['player'].position.name_short == 'MID'][0:5]
        fw = [p for p in sorted_players if p['player'].position.name_short == 'FWD'][0:3]

        remainder = sorted((df[3:5] + md[3:5] + fw[1:3]), key=lambda x: x['points'], reverse=True)[:3]

        df_pick = []
        md_pick = []
        fw_pick = []

        for player in remainder:
            if player['player'].position.name_short == "DEF":
                df_pick.append(player)
            elif player['player'].position.name_short == "MID":
                md_pick.append(player)
            if player['player'].position.name_short == "FWD":
                fw_pick.append(player)
        
        df_final = df[0:3] + df_pick
        md_final = md[0:3] + md_pick
        fw_final = [fw[0]] + fw_pick

        total = sum([player["points"] for player in gk]) + sum([player["points"] for player in df_final]) + sum([player["points"] for player in md_final]) + sum([player["points"] for player in fw_final])
        total_w_captain = total + sorted_players[0]['points']

        players_dict = {
            'gkp': gk,
            'def': df_final,
            'mid': md_final,
            'fwd': fw_final,
            'total': f"{total:,}, ({total_w_captain:,})",
            'available_gameweeks': available_gameweeks
        }

        return render(request, 'a2_fpl_data/tots.html', players_dict) 
    
class FixturesView(View):
    def get(self, request, gameweek):

        fixtures = Fixture.objects.filter(event=gameweek)

        current_gameweek = Gameweek.objects.get(is_current=True)
        gameweek_info = Gameweek.objects.get(gameweek=gameweek)
        deadline_date = gameweek_info.start_date
        deadline_time = gameweek_info.start_time

        fixture_count = {}

        for gw in range(1, 39): 
            fixture_count[gw] = Fixture.objects.filter(event=gw).count()

        fixtures_list = []

        def annotate_rank(field_name):
            return Team.objects.annotate(
            rank=Window(
                expression=Rank(),
                order_by=F(field_name).desc()
            )
        )

        overall_home_ranks = annotate_rank('strength_overall_home')
        overall_away_ranks = annotate_rank('strength_overall_away')
        attack_home_ranks = annotate_rank('strength_attack_home')
        attack_away_ranks = annotate_rank('strength_attack_away')
        defence_home_ranks = annotate_rank('strength_defence_home')
        defence_away_ranks = annotate_rank('strength_defence_away')


        for fixture in fixtures:

            for index, team in enumerate(overall_home_ranks):
                if team == fixture.team_h:
                    o_h_rank = index+1
                    break
            
            for index, team in enumerate(overall_away_ranks):
                if team == fixture.team_a:
                    o_a_rank = index+1
                    break

            for index, team in enumerate(attack_home_ranks):
                if team == fixture.team_h:
                    a_h_rank = index+1
                    break

            for index, team in enumerate(attack_away_ranks):
                if team == fixture.team_a:
                    a_a_rank = index+1
                    break

            for index, team in enumerate(defence_home_ranks):
                if team == fixture.team_h:
                    d_h_rank = index+1
                    break

            for index, team in enumerate(defence_away_ranks):
                if team == fixture.team_a:
                    d_a_rank = index+1
                    break


            fixtures_list.append({
                "event": fixture.event,
                "kickoff_date": fixture.kickoff_date,
                "kickoff_time": fixture.kickoff_time,
                "team_h": fixture.team_h,
                "team_a": fixture.team_a,
                "team_h_score": fixture.team_h_score,
                "team_a_score": fixture.team_a_score,
                "strength": {
                    "team_h_attack": {
                        "value": fixture.team_h.strength_attack_home,
                        "rank": a_h_rank,
                        "r_value": int(a_h_rank * (255 / (20 - 1))),
                        "g_value": int(255 - a_h_rank * (255 / (20 - 1)))
                    },
                    "team_h_defence": {
                        "value": fixture.team_h.strength_defence_home,
                        "rank": d_h_rank,
                        "r_value": int(d_h_rank * (255 / (20 - 1))),
                        "g_value": int(255 - (d_h_rank * (255 / (20 - 1))))
                    },
                    "team_h_overall": {
                        "value": fixture.team_h.strength_overall_home,
                        "rank": o_h_rank,
                        "r_value": int(o_h_rank * (255 / (20 - 1))),
                        "g_value": int(255 - o_h_rank * (255 / (20 - 1)))
                    },
                    "team_a_attack": {
                        "value": fixture.team_a.strength_attack_away,
                        "rank": a_a_rank,
                        "r_value": int(a_a_rank * (255 / (20 - 1))),
                        "g_value": int(255 - a_a_rank * (255 / (20 - 1)))
                    },
                    "team_a_defence": {
                        "value": fixture.team_a.strength_defence_away,
                        "rank": d_a_rank,
                        "r_value": int(d_a_rank * (255 / (20 - 1))),
                        "g_value": int(255 - d_a_rank * (255 / (20 - 1)))
                    },
                    "team_a_overall": {
                        "value": fixture.team_a.strength_overall_away,
                        "rank": o_a_rank,
                        "r_value": int(o_a_rank * (255 / (20 - 1))),
                        "g_value": int(255 - (o_a_rank * (255 / (20 - 1))))
                    }
                }        
            })

        kickoff_dates = set()

        for i in fixtures_list:
            kickoff_dates.add(i['kickoff_date'])

        kickoff_dates_list = list(kickoff_dates)

        kickoff_dates_list.sort()

        context = {
            "selected_gameweek": gameweek,
            "current_gameweek": current_gameweek,
            "deadline_date": deadline_date,
            "deadline_time": deadline_time,
            "number_of_fixtures": len(fixtures),
            "fixture_count": fixture_count,
            "available_gameweeks":  len(range(1, 39)),
            "fixtures": fixtures_list,
            "fixture_dates": kickoff_dates_list
        }

        return render(request, 'a2_fpl_data/fixtures.html', context)

class PlayerDetail(View):
    def get(self, request, player_id):

        current_gameweek = Gameweek.objects.get(is_current=True) 

        player_details = PlayerDynamicData.objects.filter(
                Q(player_id=player_id) & Q(gameweek=current_gameweek)
            )
        
        player_ranks_obj = PlayerDynamicDataRanks.objects.filter(
                Q(player_id=player_id) & Q(gameweek=current_gameweek)
            )
        
        player = player_details[0]
        player_ranks = player_ranks_obj[0]

        team = player.player.team.code
        position = player.player.position.name_short

        counts = {
                "all": PlayerDynamicData.objects.filter(Q(gameweek=current_gameweek) & ~Q(minutes=0)).count(),
                "type": PlayerDynamicData.objects.filter(Q(player_id__position__name_short=position) & Q(gameweek=current_gameweek) & ~Q(minutes=0)).count(),
                "team": PlayerDynamicData.objects.filter(Q(player_id__team__code=team) & Q(gameweek=current_gameweek) & ~Q(minutes=0)).count(),
                "team_type": PlayerDynamicData.objects.filter(Q(player_id__position__name_short=position) & Q(player_id__team__code=team) & Q(gameweek=current_gameweek) & ~Q(minutes=0)).count()
        }
            
        if player.status == "a":
            status = "Active"
            status_colour = "color: rgb(34, 149, 24);"
        elif player.status == "i":
            status = "Injured"
            status_colour = "color: rgb(219, 0, 0);"
        elif player.status == "s":
            status = "Suspended"
            status_colour = "color: rgb(219, 0, 0);"
        elif player.status == "d":
            status = "Doubtful"
            status_colour = "color: rgb(255, 230, 91);"
        elif player.status== "u":
            status = "Unavailable"
            status_colour = "color: rgb(219, 0, 0);"

        player.status = status

        context = {
            "player": player,
            "player_ranks": player_ranks,
            "counts": counts,
            "status_colour": status_colour
        }

        return render(request, 'a2_fpl_data/player.html', context)


class Teams(View):
    def get(self, request):

        teams = Team.objects.all()

        context = {
            "teams": teams
            }
        
        return render(request, 'a2_fpl_data/teams.html', context)
    
class TeamPlayerList(View):
    def get(self, request, code):

        current_gameweek = Gameweek.objects.get(is_current=True)

        team = Team.objects.filter(code=code).first()
        gkps = team.players.filter(position="1")
        defs = team.players.filter(position="2")
        mids = team.players.filter(position="3")
        fwds = team.players.filter(position="4")

        gkps_context = []
        defs_context = []
        mids_context = []
        fwds_context = []

        for player in gkps:
            player_dynamic = PlayerDynamicData.objects.filter(player_id=player.player_id, gameweek_id=current_gameweek).first()
            gkps_context.append({
                "player": player,
                "total_points": player_dynamic.total_points
            })
        
        for player in defs:
            player_dynamic = PlayerDynamicData.objects.filter(player_id=player.player_id, gameweek_id=current_gameweek).first()
            defs_context.append({
                "player": player,
                "total_points": player_dynamic.total_points
            })

        for player in mids:
            player_dynamic = PlayerDynamicData.objects.filter(player_id=player.player_id, gameweek_id=current_gameweek).first()
            mids_context.append({
                "player": player,
                "total_points": player_dynamic.total_points
            })

        for player in fwds:
            player_dynamic = PlayerDynamicData.objects.filter(player_id=player.player_id, gameweek_id=current_gameweek).first()
            fwds_context.append({
                "player": player,
                "total_points": player_dynamic.total_points
            })

        context = {
            "team": team,
            "players": {
                "gkp": gkps_context,
                "def": defs_context,
                "mid": mids_context,
                "fwd": fwds_context
            }
        }

        return render(request, 'a2_fpl_data/team.html', context)