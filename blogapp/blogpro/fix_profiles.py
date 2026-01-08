import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogpro.settings')
django.setup()

from django.contrib.auth.models import User
from users.models import Profile

def fix_profiles():
    users = User.objects.all()
    for user in users:
        # get_or_create will create if it doesn't exist
        try:
            profile, created = Profile.objects.get_or_create(user=user)
            if created:
                print(f"Created profile for {user.username}")
            else:
                print(f"Profile exists for {user.username}")
        except Exception as e:
            print(f"Error for {user.username}: {e}")

if __name__ == '__main__':
    fix_profiles()
