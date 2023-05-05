from django.urls import path
from pelatih.views import daftar_atlet, lihat_atlet, dashboard_pelatih

app_name = 'pelatih'

urlpatterns = [
    path('daftar-atlet/', daftar_atlet, name='daftar_atlet'),
    path('lihat-atlet/', lihat_atlet, name='lihat_atlet'),
    path('', dashboard_pelatih, name='dashboard_pelatih' ),

]