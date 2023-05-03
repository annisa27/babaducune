from django.urls import path
from atlet.views import daftar_sponsor

app_name = 'atlet'

urlpatterns = [
    path('daftar-sponsor/', daftar_sponsor, name='daftar_sponsor' ),

]