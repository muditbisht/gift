from django.urls import path
from .views import (
	auth, auth_login, auth_logout, auth_register
)

app_name = 'auth'
urlpatterns = (
	path('', auth, name="auth"),
	path('register/', auth_register, name="register"),
	path('login/', auth_login, name="login"),
	path('logout/', auth_logout, name="logout"),
)
