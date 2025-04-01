from django.shortcuts import render
from collections import Counter
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import ListView
from django.views import View
from django.urls import reverse_lazy
import requests
from django.shortcuts import render
from .models import Team, Region, Player, Fixture, Position, Dreamteam, Gameweek
from django.http import JsonResponse
import logging
from datetime import datetime
from django.db.models import Window, F
from django.db.models.functions import Rank

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

            # Append the player to the appropriate list based on their position
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
