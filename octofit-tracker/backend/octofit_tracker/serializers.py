from rest_framework import serializers
from .models import Team, User, Workout, Activity, Leaderboard


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['_id', 'name', 'description', 'created_at', 'member_count']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['_id', 'name', 'alias', 'email', 'team_id', 'total_points', 
                  'activities_completed', 'joined_at', 'profile_image']


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['_id', 'name', 'icon', 'unit', 'points_per_unit', 'description', 'created_at']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['_id', 'user_id', 'user_name', 'user_alias', 'workout_id', 
                  'workout_name', 'workout_icon', 'description', 'quantity', 
                  'unit', 'points_earned', 'completed_at', 'team_id']


class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ['_id', 'type', 'rank', 'entity_id', 'entity_name', 'entity_alias',
                  'team_id', 'total_points', 'activities_count', 'member_count', 'updated_at']
