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
    cost_change_event = models.FloatField(default=0)
    cost_change_start = models.FloatField(default=0)
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

    class Meta:
        unique_together = ("player", "gameweek") 

    def __str__(self):
        return f"{self.player}"
    

# Dynamic Data Ranks

class PlayerDynamicDataRanks(models.Model):
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    gameweek = models.ForeignKey(Gameweek, on_delete=models.PROTECT)

    event_points = models.JSONField(default=dict)
    total_points = models.JSONField(default=dict)
    points_per_game = models.JSONField(default=dict)

    now_cost = models.JSONField(default=dict)
    cost_change_event = models.JSONField(default=dict)
    cost_change_start = models.JSONField(default=dict)
    form = models.JSONField(default=dict)
    value_form = models.JSONField(default=dict)
    value_season = models.JSONField(default=dict)

    selected_by_percent = models.JSONField(default=dict)
    transfers_in_event = models.JSONField(default=dict)
    transfers_out_event = models.JSONField(default=dict)
    transfers_in = models.JSONField(default=dict)
    transfers_out = models.JSONField(default=dict)

    starts = models.JSONField(default=dict)
    minutes = models.JSONField(default=dict)
    goals_scored = models.JSONField(default=dict)
    assists = models.JSONField(default=dict)
    clean_sheets = models.JSONField(default=dict)
    goals_conceded = models.JSONField(default=dict)
    own_goals = models.JSONField(default=dict)
    penalties_saved = models.JSONField(default=dict)
    penalties_missed = models.JSONField(default=dict)
    yellow_cards = models.JSONField(default=dict)
    red_cards = models.JSONField(default=dict)
    saves = models.JSONField(default=dict)
    bonus = models.JSONField(default=dict)
    bps = models.JSONField(default=dict)
    goals_conceded_per_90 = models.JSONField(default=dict)
    starts_per_90 = models.JSONField(default=dict)
    clean_sheets_per_90 = models.JSONField(default=dict)
    saves_per_90 = models.JSONField(default=dict)

    expected_goals = models.JSONField(default=dict)
    expected_assists = models.JSONField(default=dict)
    expected_goal_involvements = models.JSONField(default=dict)
    expected_goals_conceded = models.JSONField(default=dict)
    expected_goals_per_90 = models.JSONField(default=dict)
    expected_assists_per_90 = models.JSONField(default=dict)
    expected_goal_involvements_per_90 = models.JSONField(default=dict)
    expected_goals_conceded_per_90 = models.JSONField(default=dict)

    influence = models.JSONField(default=dict)
    creativity = models.JSONField(default=dict)
    threat = models.JSONField(default=dict)
    ict_index = models.JSONField(default=dict)

    class Meta:
        unique_together = ("player", "gameweek")  

    def __str__(self):
        return f"{self.player}"