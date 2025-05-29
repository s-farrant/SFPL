from django.db import models

# Regions

class Region(models.Model):
    region_id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    code = models.IntegerField(unique=True)
    iso_code_short = models.CharField(max_length=2)
    iso_code_long = models.CharField(max_length=3)
    image_tag = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.name
    
# Teams

class Team(models.Model):
    code = models.IntegerField(primary_key=True, unique=True)
    team_id = models.IntegerField(null=True, unique=True)
    team_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=3)
    strength_overall_home = models.IntegerField(null=True) # Updated weekly
    strength_overall_away = models.IntegerField(null=True) # Updated weekly
    strength_attack_home = models.IntegerField(null=True) # Updated weekly
    strength_attack_away = models.IntegerField(null=True) # Updated weekly
    strength_defence_home = models.IntegerField(null=True) # Updated weekly
    strength_defence_away = models.IntegerField(null=True) # Updated weekly

    def __str__(self):
        return self.team_name
    
# Fixtures

class Fixture(models.Model):
    fixture_id = models.IntegerField(primary_key=True)
    code = models.IntegerField()
    pulse_id = models.IntegerField()
    event = models.IntegerField()
    finished = models.BooleanField()
    kickoff_date = models.DateField(null=True, default="1900-01-01")
    kickoff_time = models.TimeField(null=True, default="00:00:00")
    team_a = models.ForeignKey(Team, to_field="team_id", related_name="fixtures_a", on_delete=models.PROTECT)
    team_h = models.ForeignKey(Team, to_field="team_id", related_name="fixtures_h", on_delete=models.PROTECT)
    team_a_score = models.IntegerField(null=True)
    team_h_score = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.team_h.team_name} vs {self.team_a.team_name}"
    
# Positions

class Position(models.Model):
    position_id = models.IntegerField(primary_key=True)
    name_long = models.CharField(max_length=100)
    name_short = models.CharField(max_length=3)
    squad_select = models.IntegerField()
    squad_min_play = models.IntegerField()
    squad_max_play = models.IntegerField()

    def __str__(self):
        return self.name_short

# Players 

class Player(models.Model):
    player_id = models.IntegerField(primary_key=True)
    team = models.ForeignKey(Team, to_field="team_id", related_name="players", on_delete=models.PROTECT)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    web_name = models.CharField(max_length=100)
    squad_number = models.IntegerField(null=True)
    position = models.ForeignKey(Position, to_field="position_id", on_delete=models.PROTECT)
    photo = models.CharField(max_length=255)
    region = models.ForeignKey(Region, related_name="players", on_delete=models.PROTECT, null=True)
    birth_date = models.DateField(null=True)
    team_join_date = models.DateField(null=True)

    def __str__(self):
        return self.web_name
    
# Gameweek

class Gameweek(models.Model):
    gameweek = models.IntegerField(primary_key=True)
    start_date = models.DateField()
    start_time = models.TimeField()
    average_score = models.IntegerField(default=0, null=True)
    highest_score = models.IntegerField(default=0, null=True)
    is_previous = models.BooleanField(default=False)
    is_current = models.BooleanField(default=False)
    is_next = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    bboost_plays = models.IntegerField(default=0, null=True)
    freehit_plays = models.IntegerField(default=0, null=True)
    wildcard_plays = models.IntegerField(default=0, null=True)
    triplec_plays = models.IntegerField(default=0, null=True)
    manager_plays = models.IntegerField(default=0, null=True)
    most_selected = models.ForeignKey(Player, to_field="player_id", related_name="most_selected_gameweeks", on_delete=models.PROTECT, null=True)
    most_captained = models.ForeignKey(Player, to_field="player_id", related_name="most_captained_gameweeks", on_delete=models.PROTECT, null=True)
    most_transferred_in = models.ForeignKey(Player, to_field="player_id", related_name="most_transferred_in_gameweeks", on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"Gameweek {self.gameweek}"
    
# Dreamteam

class Dreamteam(models.Model):
    gameweek = models.ForeignKey(Gameweek, on_delete=models.PROTECT)
    player = models.ForeignKey(Player, to_field="player_id", on_delete=models.PROTECT)
    points = models.IntegerField()

    class Meta:
        unique_together = ('gameweek', 'player')
    
    def __str__(self):
        return f"{self.gameweek} - {self.player}"