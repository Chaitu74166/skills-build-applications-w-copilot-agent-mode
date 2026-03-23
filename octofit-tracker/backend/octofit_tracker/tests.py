# tests.py for Octofit Tracker
from django.test import TestCase

# Add tests for User, Team, Activity, Leaderboard, Workout here
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
	def test_create_user(self):
		user = User.objects.create(username='testuser')
		self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
	def test_create_team(self):
		team = Team.objects.create(name='Test Team')
		self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
	def test_create_activity(self):
		user = User.objects.create(username='activityuser')
		activity = Activity.objects.create(user=user, activity_type='run', duration=30, calories_burned=200, date='2024-01-01')
		self.assertEqual(activity.activity_type, 'run')

class WorkoutModelTest(TestCase):
	def test_create_workout(self):
		user = User.objects.create(username='workoutuser')
		workout = Workout.objects.create(user=user, name='Morning Workout', description='Pushups', date='2024-01-01')
		self.assertEqual(workout.name, 'Morning Workout')

class LeaderboardModelTest(TestCase):
	def test_create_leaderboard(self):
		team = Team.objects.create(name='Leaderboard Team')
		leaderboard = Leaderboard.objects.create(team=team, score=100, week=1)
		self.assertEqual(leaderboard.score, 100)
