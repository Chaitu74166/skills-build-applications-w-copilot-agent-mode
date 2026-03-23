# Models for Octofit Tracker
from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	# Extend as needed for profile fields
	pass

class Team(models.Model):
	name = models.CharField(max_length=100)
	members = models.ArrayReferenceField(to=User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

class Activity(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	activity_type = models.CharField(max_length=100)
	duration = models.IntegerField()  # in minutes
	calories_burned = models.FloatField()
	date = models.DateField()

class Workout(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	description = models.TextField()
	date = models.DateField()

class Leaderboard(models.Model):
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	score = models.FloatField()
	week = models.IntegerField()
