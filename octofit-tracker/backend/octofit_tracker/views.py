from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Team, User, Workout, Activity, Leaderboard
from .serializers import (
    TeamSerializer, UserSerializer, WorkoutSerializer,
    ActivitySerializer, LeaderboardSerializer
)


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint for teams.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at', 'member_count']
    ordering = ['name']

    @action(detail=True, methods=['get'])
    def members(self, request, pk=None):
        """Get all members of a team"""
        team = self.get_object()
        members = User.objects.filter(team_id=team._id)
        serializer = UserSerializer(members, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def activities(self, request, pk=None):
        """Get all activities for a team"""
        team = self.get_object()
        activities = Activity.objects.filter(team_id=team._id)
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['team_id']
    search_fields = ['name', 'alias', 'email']
    ordering_fields = ['name', 'total_points', 'activities_completed', 'joined_at']
    ordering = ['-total_points']

    @action(detail=True, methods=['get'])
    def activities(self, request, pk=None):
        """Get all activities for a user"""
        user = self.get_object()
        activities = Activity.objects.filter(user_id=user._id)
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    API endpoint for workout types.
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'points_per_unit']
    ordering = ['name']


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint for activities.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['user_id', 'workout_id', 'team_id']
    search_fields = ['user_name', 'user_alias', 'workout_name', 'description']
    ordering_fields = ['completed_at', 'points_earned', 'quantity']
    ordering = ['-completed_at']

    @action(detail=False, methods=['get'])
    def recent(self, request):
        """Get recent activities"""
        recent_activities = Activity.objects.all()[:20]
        serializer = self.get_serializer(recent_activities, many=True)
        return Response(serializer.data)


class LeaderboardViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for leaderboard (read-only).
    """
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['type']
    ordering_fields = ['rank', 'total_points']
    ordering = ['rank']

    @action(detail=False, methods=['get'])
    def individual(self, request):
        """Get individual leaderboard"""
        individual_leaderboard = Leaderboard.objects.filter(type='individual')
        serializer = self.get_serializer(individual_leaderboard, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def team(self, request):
        """Get team leaderboard"""
        team_leaderboard = Leaderboard.objects.filter(type='team')
        serializer = self.get_serializer(team_leaderboard, many=True)
        return Response(serializer.data)
