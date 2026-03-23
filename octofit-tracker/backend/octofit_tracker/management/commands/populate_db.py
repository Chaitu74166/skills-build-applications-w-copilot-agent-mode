from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Create users (super heroes)
        marvel_heroes = [
            {'username': 'ironman', 'email': 'ironman@marvel.com'},
            {'username': 'captainamerica', 'email': 'cap@marvel.com'},
            {'username': 'spiderman', 'email': 'spiderman@marvel.com'},
        ]
        dc_heroes = [
            {'username': 'batman', 'email': 'batman@dc.com'},
            {'username': 'superman', 'email': 'superman@dc.com'},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com'},
        ]
        marvel_users = [User.objects.create(**hero) for hero in marvel_heroes]
        dc_users = [User.objects.create(**hero) for hero in dc_heroes]

        # Create teams
        marvel_team = Team.objects.create(name='Marvel', created_at=timezone.now())
        marvel_team.members.set(marvel_users)
        dc_team = Team.objects.create(name='DC', created_at=timezone.now())
        dc_team.members.set(dc_users)

        # Create activities
        for user in marvel_users + dc_users:
            Activity.objects.create(
                user=user,
                activity_type='run',
                duration=30,
                calories_burned=300,
                date=timezone.now().date()
            )

        # Create workouts
        for user in marvel_users + dc_users:
            Workout.objects.create(
                user=user,
                name='Morning Routine',
                description='Pushups, Situps, Squats',
                date=timezone.now().date()
            )

        # Create leaderboards
        Leaderboard.objects.create(team=marvel_team, score=900, week=1)
        Leaderboard.objects.create(team=dc_team, score=850, week=1)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
