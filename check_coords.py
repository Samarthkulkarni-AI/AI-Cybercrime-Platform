import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cybercrime_platform.settings')
django.setup()

from dashboard.models import UserProfile, User

users = User.objects.all()
print(f"Total users: {users.count()}")

for user in users:
    try:
        profile = user.profile
        print(f"User: {user.username}, Address: {profile.address}, City: {profile.city}, State: {profile.state}, Pin: {profile.pincode}, Lat: {profile.latitude}, Lon: {profile.longitude}")
    except UserProfile.DoesNotExist:
        print(f"User: {user.username} has no profile.")
