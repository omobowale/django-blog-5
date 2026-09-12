import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
        
        if not all(username, email, password):
            self.stdout.write("Superuser environment variables not configured")
            return
        
        if User.objects.filter(username=username).exists():
            self.stdout.write("Superuser already exists")
            return
        
        User.objects.create_superuser(username=username, email=email, password=password)
        
        self.stdout.write("Superuser created...")
        
        
    