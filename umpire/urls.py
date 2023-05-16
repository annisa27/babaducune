from django.urls import path
from umpire.views import list_event, dashboard_umpire, hasil_pertandingan, detail_hasil_pertandingan, pertandingan, form_buat_ujian_kualifikasi, list_ujian_kualifikasi_umpire

app_name = 'umpire'

urlpatterns = [
    path('list-event/', list_event, name='list_event'),
    path('list-event/pertandingan/', pertandingan, name='pertandingan'),
    path('hasil-pertandingan/', hasil_pertandingan, name='hasil_pertandingan'),
    path('hasil-pertandingan/detail/', detail_hasil_pertandingan, name='detail_hasil_pertandingan'),
    path('', dashboard_umpire, name='dashboard_umpire' ),
    path('form-buat-ujian-kualifikasi/', form_buat_ujian_kualifikasi, name='form_buat_ujian_kualifikasi' ),
    path('list-ujian-kualifikasi-umpire/', list_ujian_kualifikasi_umpire, name='list_ujian_kualifikasi_umpire' ),

]