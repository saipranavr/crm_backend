# BL/auth_service.py
from django.contrib.auth import authenticate, login, logout
from crm.DL.user_repository import UserRepository

class AuthService:
    @staticmethod
    def login_user(request, email, password):
        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return True
        return False

    @staticmethod
    def logout_user(request):
        logout(request)

    @staticmethod
    def register_user(email, password):
        if UserRepository.find_by_email(email) is None:
            return UserRepository.create_user(email, password)
        return None
