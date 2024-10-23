# DL/user_repository.py
from crm.models.user import User

class UserRepository:
    @staticmethod
    def find_by_email(email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    @staticmethod
    def create_user(email, password):
        user = User.objects.create_user(email=email, password=password)
        return user
