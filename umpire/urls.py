from django.urls import path
from umpire.views import list_event, dashboard

app_name = 'umpire'

urlpatterns = [
    path('list-event/', list_event, name='list_event'),
    path('dashboard/', dashboard, name='dashboard' ),

]