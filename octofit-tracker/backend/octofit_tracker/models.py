from djongo import models


class Team(models.Model):
    _id = models.CharField(max_length=100, primary_key=True, db_column='_id')
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField()
    member_count = models.IntegerField(default=0)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class User(models.Model):
    _id = models.CharField(max_length=100, primary_key=True, db_column='_id')
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    team_id = models.CharField(max_length=100)
    total_points = models.IntegerField(default=0)
    activities_completed = models.IntegerField(default=0)
    joined_at = models.DateTimeField()
    profile_image = models.URLField(max_length=500, blank=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"{self.name} ({self.alias})"


class Workout(models.Model):
    _id = models.CharField(max_length=100, primary_key=True, db_column='_id')
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=10)
    unit = models.CharField(max_length=50)
    points_per_unit = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return f"{self.icon} {self.name}"


class Activity(models.Model):
    _id = models.CharField(max_length=100, primary_key=True, db_column='_id')
    user_id = models.CharField(max_length=100)
    user_name = models.CharField(max_length=200)
    user_alias = models.CharField(max_length=200)
    workout_id = models.CharField(max_length=100)
    workout_name = models.CharField(max_length=200)
    workout_icon = models.CharField(max_length=10)
    description = models.TextField()
    quantity = models.IntegerField()
    unit = models.CharField(max_length=50)
    points_earned = models.IntegerField()
    completed_at = models.DateTimeField()
    team_id = models.CharField(max_length=100)

    class Meta:
        db_table = 'activities'
        ordering = ['-completed_at']

    def __str__(self):
        return f"{self.user_alias}: {self.workout_name} - {self.quantity} {self.unit}"


class Leaderboard(models.Model):
    _id = models.CharField(max_length=100, primary_key=True, db_column='_id')
    type = models.CharField(max_length=50)  # 'individual' or 'team'
    rank = models.IntegerField()
    entity_id = models.CharField(max_length=100)
    entity_name = models.CharField(max_length=200)
    entity_alias = models.CharField(max_length=200, blank=True, null=True)
    team_id = models.CharField(max_length=100, blank=True, null=True)
    total_points = models.IntegerField()
    activities_count = models.IntegerField(blank=True, null=True)
    member_count = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'leaderboard'
        ordering = ['rank']

    def __str__(self):
        return f"{self.type.capitalize()} - Rank {self.rank}: {self.entity_name}"
