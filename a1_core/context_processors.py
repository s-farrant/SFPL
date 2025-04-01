from a2_fpl_data.models import Gameweek

def current_gameweek(request):

    gameweek = Gameweek.objects.filter(is_current=True).first()

    context = {
        "gameweek": gameweek.gameweek,
        "gameweek_previous": gameweek.gameweek-1,
        "gameweek_next": gameweek.gameweek+1,
        "finished": gameweek.finished
    }

    return context