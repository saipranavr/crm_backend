# views.py
from django.urls import path
from crm.controllers.auth_controller import login_view, logout_view, register_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]

# templates/login.html
<form method="post">
    {% csrf_token %}
    <input type="email" name="email" placeholder="Email" required>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit">Login</button>
    {% if error %}<p>{{ error }}</p>{% endif %}
</form>
