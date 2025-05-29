from a2_fpl_data.models import Gameweek

def current_gameweek(request):

    gameweek = Gameweek.objects.filter(is_current=True).first()

    gameweek_next = min(38, gameweek.gameweek+1)
    gameweek_previous = max(1, gameweek.gameweek-1)

    context = {
        "gameweek": gameweek.gameweek,
        "gameweek_previous": gameweek_previous,
        "gameweek_next": gameweek_next,
        "finished": gameweek.finished
    }

    return context