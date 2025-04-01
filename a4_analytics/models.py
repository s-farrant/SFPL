from django.db import models
from a2_fpl_data.models import Player, Gameweek

# Create your models here.

# All dynamic data

class PlayerDynamicData(models.Model):
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    gameweek = models.ForeignKey(Gameweek, on_delete=models.PROTECT)
    event_points = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
    ep_next = models.FloatField(default=0)
    points_per_game = models.FloatField(default=0)

    now_cost = models.FloatField(default=0)
    cost_change_event = models.IntegerField(default=0)
    cost_change_start = models.IntegerField(default=0)
    form = models.FloatField(default=0)
    value_form = models.FloatField(default=0)
    value_season = models.FloatField(default=0)

    selected_by_percent = models.FloatField(default=0)
    transfers_in_event = models.IntegerField(default=0)
    transfers_out_event = models.IntegerField(default=0)
    transfers_in = models.IntegerField(default=0)
    transfers_out = models.IntegerField(default=0)

    status = models.CharField(max_length=1, default="a")

    starts = models.IntegerField(default=0)
    minutes = models.IntegerField(default=0)
    goals_scored = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    clean_sheets = models.IntegerField(default=0)
    goals_conceded = models.IntegerField(default=0)
    own_goals = models.IntegerField(default=0)
    penalties_saved = models.IntegerField(default=0)
    penalties_missed = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)
    saves = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    bps = models.IntegerField(default=0)
    goals_conceded_per_90 = models.FloatField(default=0)
    starts_per_90 = models.FloatField(default=0)
    clean_sheets_per_90 = models.FloatField(default=0)
    saves_per_90 = models.FloatField(default=0)

    expected_goals = models.FloatField(default=0)
    expected_assists = models.FloatField(default=0)
    expected_goal_involvements = models.FloatField(default=0)
    expected_goals_conceded = models.FloatField(default=0)
    expected_goals_per_90 = models.FloatField(default=0)
    expected_assists_per_90 = models.FloatField(default=0)
    expected_goal_involvements_per_90 = models.FloatField(default=0)
    expected_goals_conceded_per_90 = models.FloatField(default=0)

    influence = models.FloatField(default=0)
    creativity = models.FloatField(default=0)
    threat = models.FloatField(default=0)
    ict_index = models.FloatField(default=0)

    influence_rank = models.IntegerField(default=0)
    influence_rank_type = models.IntegerField(default=0)
    creativity_rank = models.IntegerField(default=0)
    creativity_rank_type = models.IntegerField(default=0)
    threat_rank = models.IntegerField(default=0)
    threat_rank_type = models.IntegerField(default=0)
    ict_index_rank = models.IntegerField(default=0)
    ict_index_rank_type = models.IntegerField(default=0)

    now_cost_rank = models.IntegerField(default=0)
    now_cost_rank_type = models.IntegerField(default=0)
    form_rank = models.IntegerField(default=0)
    form_rank_type = models.IntegerField(default=0)
    points_per_game_rank = models.IntegerField(default=0)
    points_per_game_rank_type = models.IntegerField(default=0)
    selected_rank = models.IntegerField(default=0)
    selected_rank_type = models.IntegerField(default=0)

    class Meta:
        unique_together = ("player", "gameweek")  # Avoid duplicate player-gameweek records

    def __str__(self):
        return f"{self.player}"