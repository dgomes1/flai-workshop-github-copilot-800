from django.contrib import admin
from .models import Team, User, Workout, Activity, Leaderboard


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('_id', 'name', 'description', 'member_count', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
    ordering = ('name',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('_id', 'name', 'alias', 'email', 'team_id', 'total_points', 'activities_completed', 'joined_at')
    search_fields = ('name', 'alias', 'email')
    list_filter = ('team_id', 'joined_at')
    ordering = ('-total_points',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('_id', 'name', 'icon', 'unit', 'points_per_unit', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
    ordering = ('name',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('_id', 'user_alias', 'workout_name', 'quantity', 'unit', 'points_earned', 'completed_at', 'team_id')
    search_fields = ('user_name', 'user_alias', 'workout_name', 'description')
    list_filter = ('workout_name', 'team_id', 'completed_at')
    ordering = ('-completed_at',)


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('_id', 'type', 'rank', 'entity_name', 'total_points', 'updated_at')
    search_fields = ('entity_name', 'entity_alias')
    list_filter = ('type', 'updated_at')
    ordering = ('rank',)
