"""
URL configuration for sfpl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from a1_core.views import HomeView
from a2_fpl_data.views import DreamteamView, FixturesView, TOTS, PlayerDetail, Teams, TeamPlayerList
from a4_analytics.views import ICT, InGame, Transfers, PlayerValue
from a5_predictions.views import EpNextView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView, name='home'),
    path('dreamteam/<int:gameweek>/', DreamteamView.as_view(), name='dreamteam'),
    path('ep/', EpNextView.as_view(), name="ep"),
    path('fixtures/<int:gameweek>/', FixturesView.as_view(), name="fixtures"),
    path('ict/', ICT.as_view(), name='ict'),
    path('in-game/', InGame.as_view(), name='in-game'),
    path('transfers/', Transfers.as_view(), name='transfers'),
    path('player-value/', PlayerValue.as_view(), name='player-value'),
    path('overall/', TOTS.as_view(), name='tots'),
    path('player/<int:player_id>', PlayerDetail.as_view(), name='player'),
    path('teams/', Teams.as_view(), name='teams'),
    path('teams/<int:code>', TeamPlayerList.as_view(), name='player_list'),
]
