from django.urls import path
from users.views import *

app_name = 'users'

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('registration/', RegisterUserView.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('logout/', logoutuser, name='logout'),
]
