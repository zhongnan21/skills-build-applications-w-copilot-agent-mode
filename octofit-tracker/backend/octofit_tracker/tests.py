from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel')
        self.assertEqual(team.name, 'Marvel')

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name='DC')
        user = User.objects.create(name='Superman', email='superman@dc.com', team=team)
        self.assertEqual(user.name, 'Superman')
        self.assertEqual(user.team.name, 'DC')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=team)
        activity = Activity.objects.create(user=user, type='Running', duration=30, calories=300, date='2025-09-02')
        self.assertEqual(activity.type, 'Running')
        self.assertEqual(activity.user.name, 'Iron Man')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Cardio', description='Cardio workout')
        self.assertEqual(workout.name, 'Cardio')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Marvel')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.team.name, 'Marvel')
        self.assertEqual(leaderboard.points, 100)
