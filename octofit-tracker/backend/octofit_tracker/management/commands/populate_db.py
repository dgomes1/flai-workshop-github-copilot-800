from django.core.management.base import BaseCommand
from pymongo import MongoClient
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Clear existing data
        self.stdout.write(self.style.WARNING('Clearing existing data...'))
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create unique index on email field
        self.stdout.write('Creating unique index on email field...')
        db.users.create_index([("email", 1)], unique=True)

        # Define teams
        teams_data = [
            {
                '_id': 'team_marvel',
                'name': 'Team Marvel',
                'description': 'Earth\'s Mightiest Heroes',
                'created_at': datetime.now(),
                'member_count': 0
            },
            {
                '_id': 'team_dc',
                'name': 'Team DC',
                'description': 'Justice League United',
                'created_at': datetime.now(),
                'member_count': 0
            }
        ]

        # Define users (superheroes)
        marvel_heroes = [
            {'name': 'Tony Stark', 'alias': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'team_marvel'},
            {'name': 'Steve Rogers', 'alias': 'Captain America', 'email': 'cap@marvel.com', 'team': 'team_marvel'},
            {'name': 'Bruce Banner', 'alias': 'Hulk', 'email': 'hulk@marvel.com', 'team': 'team_marvel'},
            {'name': 'Natasha Romanoff', 'alias': 'Black Widow', 'email': 'blackwidow@marvel.com', 'team': 'team_marvel'},
            {'name': 'Thor Odinson', 'alias': 'Thor', 'email': 'thor@marvel.com', 'team': 'team_marvel'},
            {'name': 'Peter Parker', 'alias': 'Spider-Man', 'email': 'spidey@marvel.com', 'team': 'team_marvel'},
        ]

        dc_heroes = [
            {'name': 'Clark Kent', 'alias': 'Superman', 'email': 'superman@dc.com', 'team': 'team_dc'},
            {'name': 'Bruce Wayne', 'alias': 'Batman', 'email': 'batman@dc.com', 'team': 'team_dc'},
            {'name': 'Diana Prince', 'alias': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'team_dc'},
            {'name': 'Barry Allen', 'alias': 'Flash', 'email': 'flash@dc.com', 'team': 'team_dc'},
            {'name': 'Arthur Curry', 'alias': 'Aquaman', 'email': 'aquaman@dc.com', 'team': 'team_dc'},
            {'name': 'Hal Jordan', 'alias': 'Green Lantern', 'email': 'greenlantern@dc.com', 'team': 'team_dc'},
        ]

        all_heroes = marvel_heroes + dc_heroes
        users_data = []

        for i, hero in enumerate(all_heroes, start=1):
            user = {
                '_id': f'user_{i}',
                'name': hero['name'],
                'alias': hero['alias'],
                'email': hero['email'],
                'team_id': hero['team'],
                'total_points': random.randint(500, 2000),
                'activities_completed': random.randint(10, 50),
                'joined_at': datetime.now() - timedelta(days=random.randint(1, 90)),
                'profile_image': f'https://api.dicebear.com/7.x/avataaars/svg?seed={hero["alias"]}'
            }
            users_data.append(user)

        # Update team member counts
        teams_data[0]['member_count'] = len(marvel_heroes)
        teams_data[1]['member_count'] = len(dc_heroes)

        # Define workout types
        workout_types = [
            {'name': 'Running', 'icon': '🏃', 'unit': 'km', 'points_per_unit': 10},
            {'name': 'Cycling', 'icon': '🚴', 'unit': 'km', 'points_per_unit': 5},
            {'name': 'Swimming', 'icon': '🏊', 'unit': 'laps', 'points_per_unit': 15},
            {'name': 'Push-ups', 'icon': '💪', 'unit': 'reps', 'points_per_unit': 1},
            {'name': 'Weightlifting', 'icon': '🏋️', 'unit': 'kg', 'points_per_unit': 2},
            {'name': 'Yoga', 'icon': '🧘', 'unit': 'minutes', 'points_per_unit': 5},
            {'name': 'Boxing', 'icon': '🥊', 'unit': 'rounds', 'points_per_unit': 20},
        ]

        workouts_data = []
        for i, workout in enumerate(workout_types, start=1):
            workout['_id'] = f'workout_{i}'
            workout['description'] = f'{workout["name"]} exercise'
            workout['created_at'] = datetime.now()
            workouts_data.append(workout)

        # Define activities
        activities_data = []
        activity_descriptions = {
            'Running': ['Morning run in the park', 'Evening jog', 'Sprint training', 'Marathon prep'],
            'Cycling': ['Bike to work', 'Mountain biking', 'Road cycling', 'City tour'],
            'Swimming': ['Pool training', 'Open water swim', 'Lap practice', 'Endurance swim'],
            'Push-ups': ['Daily routine', 'Chest workout', 'Upper body training', 'Challenge completed'],
            'Weightlifting': ['Leg day', 'Arm workout', 'Back exercises', 'Full body workout'],
            'Yoga': ['Morning stretch', 'Meditation session', 'Flexibility training', 'Relaxation'],
            'Boxing': ['Training session', 'Sparring practice', 'Heavy bag workout', 'Speed training'],
        }

        for i in range(1, 101):  # Create 100 activities
            user = random.choice(users_data)
            workout = random.choice(workouts_data)
            quantity = random.randint(1, 50)
            points = quantity * workout['points_per_unit']

            activity = {
                '_id': f'activity_{i}',
                'user_id': user['_id'],
                'user_name': user['name'],
                'user_alias': user['alias'],
                'workout_id': workout['_id'],
                'workout_name': workout['name'],
                'workout_icon': workout['icon'],
                'description': random.choice(activity_descriptions[workout['name']]),
                'quantity': quantity,
                'unit': workout['unit'],
                'points_earned': points,
                'completed_at': datetime.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 23)),
                'team_id': user['team_id']
            }
            activities_data.append(activity)

        # Calculate leaderboard data
        leaderboard_data = []
        
        # Individual leaderboard
        sorted_users = sorted(users_data, key=lambda x: x['total_points'], reverse=True)
        for rank, user in enumerate(sorted_users, start=1):
            leaderboard_entry = {
                '_id': f'leaderboard_user_{rank}',
                'type': 'individual',
                'rank': rank,
                'entity_id': user['_id'],
                'entity_name': user['name'],
                'entity_alias': user['alias'],
                'team_id': user['team_id'],
                'total_points': user['total_points'],
                'activities_count': user['activities_completed'],
                'updated_at': datetime.now()
            }
            leaderboard_data.append(leaderboard_entry)

        # Team leaderboard
        team_marvel_points = sum(u['total_points'] for u in users_data if u['team_id'] == 'team_marvel')
        team_dc_points = sum(u['total_points'] for u in users_data if u['team_id'] == 'team_dc')

        team_leaderboard = [
            {
                '_id': 'leaderboard_team_1',
                'type': 'team',
                'rank': 1 if team_marvel_points > team_dc_points else 2,
                'entity_id': 'team_marvel',
                'entity_name': 'Team Marvel',
                'total_points': team_marvel_points,
                'member_count': len(marvel_heroes),
                'updated_at': datetime.now()
            },
            {
                '_id': 'leaderboard_team_2',
                'type': 'team',
                'rank': 1 if team_dc_points > team_marvel_points else 2,
                'entity_id': 'team_dc',
                'entity_name': 'Team DC',
                'total_points': team_dc_points,
                'member_count': len(dc_heroes),
                'updated_at': datetime.now()
            }
        ]
        
        # Sort team leaderboard by rank
        team_leaderboard.sort(key=lambda x: x['rank'])
        leaderboard_data.extend(team_leaderboard)

        # Insert data into collections
        self.stdout.write('Inserting teams...')
        db.teams.insert_many(teams_data)
        self.stdout.write(self.style.SUCCESS(f'✓ Inserted {len(teams_data)} teams'))

        self.stdout.write('Inserting users...')
        db.users.insert_many(users_data)
        self.stdout.write(self.style.SUCCESS(f'✓ Inserted {len(users_data)} users'))

        self.stdout.write('Inserting workouts...')
        db.workouts.insert_many(workouts_data)
        self.stdout.write(self.style.SUCCESS(f'✓ Inserted {len(workouts_data)} workouts'))

        self.stdout.write('Inserting activities...')
        db.activities.insert_many(activities_data)
        self.stdout.write(self.style.SUCCESS(f'✓ Inserted {len(activities_data)} activities'))

        self.stdout.write('Inserting leaderboard entries...')
        db.leaderboard.insert_many(leaderboard_data)
        self.stdout.write(self.style.SUCCESS(f'✓ Inserted {len(leaderboard_data)} leaderboard entries'))

        self.stdout.write(self.style.SUCCESS('\n✅ Database population completed successfully!'))
        self.stdout.write(f'\nSummary:')
        self.stdout.write(f'  - Teams: {len(teams_data)}')
        self.stdout.write(f'  - Users: {len(users_data)}')
        self.stdout.write(f'  - Workouts: {len(workouts_data)}')
        self.stdout.write(f'  - Activities: {len(activities_data)}')
        self.stdout.write(f'  - Leaderboard entries: {len(leaderboard_data)}')

        client.close()
