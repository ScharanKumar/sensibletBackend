# core/utils.py

from django.contrib.auth.models import User

def get_user_id_by_username(username):
    try:
        # Query the user by username
        user = User.objects.get(username=username)
        
        # Access the user's ID
        return user.id
    except User.DoesNotExist:
        return "User not found"
