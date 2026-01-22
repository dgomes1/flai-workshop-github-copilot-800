"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import os
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .views import TeamViewSet, UserViewSet, WorkoutViewSet, ActivityViewSet, LeaderboardViewSet


@api_view(['GET'])
def api_root(request, format=None):
    """
    API Root - OctoFit Tracker API
    """
    # Construct base URL using CODESPACE_NAME if available
    codespace_name = os.getenv('CODESPACE_NAME')
    if codespace_name:
        base_url = f'https://{codespace_name}-8000.app.github.dev/'
    else:
        base_url = request.build_absolute_uri('/')
    
    return Response({
        'teams': f'{base_url}api/teams/',
        'users': f'{base_url}api/users/',
        'workouts': f'{base_url}api/workouts/',
        'activities': f'{base_url}api/activities/',
        'leaderboard': f'{base_url}api/leaderboard/',
    })


# Create a router and register our viewsets
router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'users', UserViewSet, basename='user')
router.register(r'workouts', WorkoutViewSet, basename='workout')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
