from django.db import models

class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)

class User(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')

class Activity(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
	type = models.CharField(max_length=50)
	duration = models.IntegerField()  # minutes
	calories = models.IntegerField()
	date = models.DateField()

class Workout(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	suggested_for = models.ManyToManyField(User, related_name='suggested_workouts')

class Leaderboard(models.Model):
	team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard')
	points = models.IntegerField()
