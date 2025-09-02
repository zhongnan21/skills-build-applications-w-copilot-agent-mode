from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        with transaction.atomic():
            # Clear existing data
            Leaderboard.objects.all().delete()
            Activity.objects.all().delete()
            Workout.objects.all().delete()
            User.objects.all().delete()
            Team.objects.all().delete()

            # Create teams
            marvel = Team.objects.create(name='Marvel')
            dc = Team.objects.create(name='DC')

            # Create users
            users = [
                User(name='Iron Man', email='ironman@marvel.com', team=marvel),
                User(name='Captain America', email='cap@marvel.com', team=marvel),
                User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
                User(name='Superman', email='superman@dc.com', team=dc),
                User(name='Batman', email='batman@dc.com', team=dc),
                User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            ]
            User.objects.bulk_create(users)

            # Create activities
            for user in User.objects.all():
                Activity.objects.create(user=user, type='Running', duration=30, calories=300, date='2025-09-02')
                Activity.objects.create(user=user, type='Cycling', duration=45, calories=400, date='2025-09-01')

            # Create workouts
            workout1 = Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout')
            workout2 = Workout.objects.create(name='Strength Training', description='Full body strength workout')
            for user in User.objects.all():
                workout1.suggested_for.add(user)
                workout2.suggested_for.add(user)

            # Create leaderboard
            Leaderboard.objects.create(team=marvel, points=250)
            Leaderboard.objects.create(team=dc, points=200)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
