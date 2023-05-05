from django.urls import path
from atlet.views import daftar_sponsor, form_tes_kualifikasi, tes_kualifikasi, daftar_event, detail_stadium, detail_event, dashboard

app_name = 'atlet'

urlpatterns = [
    path('daftar-sponsor/', daftar_sponsor, name='daftar_sponsor' ),
    path('form-kualifikasi/', form_tes_kualifikasi, name='form_tes_kualifikasi' ),
    path('tes-kualifikasi/', tes_kualifikasi, name='tes_kualifikasi' ),
    path('daftar-event/stadium', daftar_event, name='daftar_event' ),
    path('daftar-event/stadium/event/', detail_stadium, name='detail_stadium' ),
    path('daftar-event/stadium/event/kategori', detail_event, name='detail_event' ),
    path('dashboard/', dashboard, name='dashboard' ),
]