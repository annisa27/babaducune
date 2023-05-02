from django.urls import path
from authentication.views import show_login, show_register, show_home

app_name = 'authentication'

urlpatterns = [
    path('', show_home, name='show_home'),
    path('register/', show_register, name='show_register' ),
    path('login/', show_login, name='show_login' ),
]