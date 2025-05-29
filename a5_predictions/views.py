from django.shortcuts import render
from django.http import HttpResponse
from a2_fpl_data.models import Fixture
from a4_analytics.models import PlayerDynamicData
from django.views import View
from django.db.models import Q
import json

# Create your views here. 

class EpNextView(View):
    def get(self, request):

        selected_position = request.GET.get('position', 'all')

        latest_gameweek = PlayerDynamicData.objects.order_by('-gameweek').values_list('gameweek', flat=True).first()
        players_latest_gameweek = PlayerDynamicData.objects.filter(gameweek=latest_gameweek)

        gk = []
        df = []
        mf = []
        fw = []
    
        for entry in players_latest_gameweek:

            player = entry.player
            position = entry.player.position
            team = player.team

            fixtures = Fixture.objects.filter(
                Q(team_h=player.team) | Q(team_a=player.team),
                event=int(latest_gameweek+1)
            )
            

            opponent = None
            location = None
            opponent2 = None
            location2 = None
            oppo_loc = None
            oppo_loc2 = None
            for fixture in fixtures:
                if len(fixtures) == 1:
                    if fixture.team_h == player.team:
                        opponent = fixture.team_a.short_name
                        location = "Home"
                        oppo_loc = "A"
                    elif fixture.team_a == player.team:
                        opponent = fixture.team_h.short_name
                        location = "Away"
                        oppo_loc = "H"
                elif len(fixtures) == 2:
                    if opponent == None:
                        if fixture.team_h == player.team:
                            opponent = fixture.team_a.short_name
                            location = "Home"
                            oppo_loc = "A"
                        elif fixture.team_a == player.team:
                            opponent = fixture.team_h.short_name
                            location = "Away"
                            oppo_loc = "H"
                    else:
                        if fixture.team_h == player.team:
                            opponent2 = fixture.team_a.short_name
                            location2 = "Home"
                            oppo_loc2 = "A"
                        elif fixture.team_a == player.team:
                            opponent2 = fixture.team_h.short_name
                            location2 = "Away"
                            oppo_loc2 = "H"
                else:
                    pass

            if player.position.name_short == "GKP":
                gk.append({
                    "player": player,
                    "team": team,
                    "position": position,
                    "ep_next": entry.ep_next,
                    "opponent": opponent,
                    "location": location,
                    "opponent2": opponent2,
                    "location2": location2,
                    "oppo_loc": oppo_loc,
                    "oppo_loc2": oppo_loc2
                    }
                )
            if player.position.name_short == "DEF":
                df.append({
                    "player": player,
                    "team": team,
                    "position": player.position.name_short,
                    "ep_next": entry.ep_next,
                    "opponent": opponent,
                    "location": location,
                    "opponent2": opponent2,
                    "location2": location2,
                    "oppo_loc": oppo_loc,
                    "oppo_loc2": oppo_loc2
                    }
                )
            if player.position.name_short == "MID":
                mf.append({
                    "player": player,
                    "team": team,
                    "position": player.position.name_short,
                    "ep_next": entry.ep_next,
                    "opponent": opponent,
                    "location": location,
                    "opponent2": opponent2,
                    "location2": location2,
                    "oppo_loc": oppo_loc,
                    "oppo_loc2": oppo_loc2
                    }
                )
            if player.position.name_short == "FWD":
                fw.append({
                    "player": player,
                    "team": team,
                    "position": player.position.name_short,
                    "ep_next": entry.ep_next,
                    "opponent": opponent,
                    "location": location,
                    "opponent2": opponent2,
                    "location2": location2,
                    "oppo_loc": oppo_loc,
                    "oppo_loc2": oppo_loc2
                    }
                )

        sorted_gk = sorted(gk, key=lambda x: x['ep_next'], reverse=True)
        sorted_df = sorted(df, key=lambda x: x['ep_next'], reverse=True)
        sorted_md = sorted(mf, key=lambda x: x['ep_next'], reverse=True)
        sorted_fw = sorted(fw, key=lambda x: x['ep_next'], reverse=True)


        top_gk = sorted_gk[:1]
        top_df = sorted_df[:3]
        top_mf = sorted_md[:3]
        top_fw = sorted_fw[:1]

        next_df = sorted_df[3:5]
        next_mf = sorted_md[3:5]
        next_fw = sorted_fw[1:3]

        next_all = next_df + next_mf + next_fw
        sorted_next_all = sorted(next_all, key=lambda x: x['ep_next'], reverse=True)
        sorted_next_top = sorted_next_all[:3]

        for i in sorted_next_top:
            if i['position'] == 'DEF':
                top_df.append(i)
            elif i['position'] == 'MID':
                top_mf.append(i)
            elif i['position'] == 'FWD':
                top_fw.append(i)    

        all = gk + df + mf + fw 

        sorted_all = sorted(all, key=lambda x: x['ep_next'], reverse=True)

        total = 0

        for j in top_gk:
            total += int(j['ep_next'])
        for k in top_df:
            total += int(k['ep_next'])
        for l in top_mf:
            total += int(l['ep_next'])
        for m in top_fw:
            total += int(m['ep_next'])

        context = {
            "all": sorted_all,
            "all_gkp": sorted_gk,
            "all_def": sorted_df,
            "all_mid": sorted_md,
            "all_fwd": sorted_fw,
            "gkp": top_gk,
            "def": top_df,
            "mid": top_mf,
            "fwd": top_fw,
            "total": total,
            "selected-position": selected_position
        }

        return render(request, 'a5_predictions/expected_points.html', context)