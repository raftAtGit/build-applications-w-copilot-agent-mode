from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            self.stdout.write(self.style.WARNING('Deleting old data...'))
            User.objects.all().delete()
            Team.objects.all().delete()
            Activity.objects.all().delete()
            Leaderboard.objects.all().delete()
            Workout.objects.all().delete()

            self.stdout.write(self.style.SUCCESS('Creating teams...'))
            marvel = Team.objects.create(name='marvel')
            dc = Team.objects.create(name='dc')

            self.stdout.write(self.style.SUCCESS('Creating users...'))
            users = [
                User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel.name),
                User.objects.create(email='captainamerica@marvel.com', name='Captain America', team=marvel.name),
                User.objects.create(email='batman@dc.com', name='Batman', team=dc.name),
                User.objects.create(email='superman@dc.com', name='Superman', team=dc.name),
            ]

            self.stdout.write(self.style.SUCCESS('Creating activities...'))
            Activity.objects.create(user=users[0].email, activity_type='run', duration=30, date='2025-01-01')
            Activity.objects.create(user=users[1].email, activity_type='cycle', duration=45, date='2025-01-02')
            Activity.objects.create(user=users[2].email, activity_type='swim', duration=60, date='2025-01-03')
            Activity.objects.create(user=users[3].email, activity_type='yoga', duration=20, date='2025-01-04')

            self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
            Leaderboard.objects.create(user=users[0].email, score=100)
            Leaderboard.objects.create(user=users[1].email, score=90)
            Leaderboard.objects.create(user=users[2].email, score=110)
            Leaderboard.objects.create(user=users[3].email, score=95)

            self.stdout.write(self.style.SUCCESS('Creating workouts...'))
            Workout.objects.create(name='Pushups', description='Do 20 pushups')
            Workout.objects.create(name='Situps', description='Do 30 situps')
            Workout.objects.create(name='Squats', description='Do 40 squats')

            self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
