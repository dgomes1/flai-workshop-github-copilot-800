from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Team, User, Workout, Activity, Leaderboard
from datetime import datetime


class TeamModelTest(TestCase):
    """Test Team model"""
    
    def setUp(self):
        self.team = Team.objects.create(
            _id='test_team',
            name='Test Team',
            description='A test team',
            created_at=datetime.now(),
            member_count=0
        )

    def test_team_creation(self):
        """Test that a team can be created"""
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(str(self.team), 'Test Team')


class UserModelTest(TestCase):
    """Test User model"""
    
    def setUp(self):
        self.user = User.objects.create(
            _id='test_user',
            name='Test User',
            alias='Test Hero',
            email='test@test.com',
            team_id='test_team',
            total_points=100,
            activities_completed=5,
            joined_at=datetime.now()
        )

    def test_user_creation(self):
        """Test that a user can be created"""
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.alias, 'Test Hero')
        self.assertEqual(str(self.user), 'Test User (Test Hero)')


class WorkoutModelTest(TestCase):
    """Test Workout model"""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            _id='test_workout',
            name='Test Workout',
            icon='🏃',
            unit='km',
            points_per_unit=10,
            description='A test workout',
            created_at=datetime.now()
        )

    def test_workout_creation(self):
        """Test that a workout can be created"""
        self.assertEqual(self.workout.name, 'Test Workout')
        self.assertEqual(str(self.workout), '🏃 Test Workout')


class TeamAPITest(APITestCase):
    """Test Team API endpoints"""
    
    def setUp(self):
        self.team = Team.objects.create(
            _id='api_test_team',
            name='API Test Team',
            description='API test team description',
            created_at=datetime.now(),
            member_count=0
        )

    def test_get_teams_list(self):
        """Test retrieving the teams list"""
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_team_detail(self):
        """Test retrieving a single team"""
        url = reverse('team-detail', args=[self.team._id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'API Test Team')


class UserAPITest(APITestCase):
    """Test User API endpoints"""
    
    def setUp(self):
        self.user = User.objects.create(
            _id='api_test_user',
            name='API Test User',
            alias='API Hero',
            email='apitest@test.com',
            team_id='test_team',
            total_points=200,
            activities_completed=10,
            joined_at=datetime.now()
        )

    def test_get_users_list(self):
        """Test retrieving the users list"""
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_user_detail(self):
        """Test retrieving a single user"""
        url = reverse('user-detail', args=[self.user._id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'API Test User')


class WorkoutAPITest(APITestCase):
    """Test Workout API endpoints"""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            _id='api_test_workout',
            name='API Test Workout',
            icon='💪',
            unit='reps',
            points_per_unit=5,
            description='API test workout',
            created_at=datetime.now()
        )

    def test_get_workouts_list(self):
        """Test retrieving the workouts list"""
        url = reverse('workout-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class ActivityAPITest(APITestCase):
    """Test Activity API endpoints"""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            _id='api_test_activity',
            user_id='test_user',
            user_name='Test User',
            user_alias='Test Hero',
            workout_id='test_workout',
            workout_name='Test Workout',
            workout_icon='🏃',
            description='Test activity',
            quantity=10,
            unit='km',
            points_earned=100,
            completed_at=datetime.now(),
            team_id='test_team'
        )

    def test_get_activities_list(self):
        """Test retrieving the activities list"""
        url = reverse('activity-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class LeaderboardAPITest(APITestCase):
    """Test Leaderboard API endpoints"""
    
    def setUp(self):
        self.leaderboard_entry = Leaderboard.objects.create(
            _id='api_test_leaderboard',
            type='individual',
            rank=1,
            entity_id='test_user',
            entity_name='Test User',
            entity_alias='Test Hero',
            team_id='test_team',
            total_points=500,
            activities_count=20,
            updated_at=datetime.now()
        )

    def test_get_leaderboard_list(self):
        """Test retrieving the leaderboard list"""
        url = reverse('leaderboard-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_individual_leaderboard(self):
        """Test retrieving individual leaderboard"""
        url = reverse('leaderboard-individual')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class APIRootTest(APITestCase):
    """Test API root endpoint"""
    
    def test_api_root(self):
        """Test that API root returns all endpoint links"""
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('teams', response.data)
        self.assertIn('users', response.data)
        self.assertIn('workouts', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
