from django.urls import path
from atlet.views import daftar_sponsor, form_tes_kualifikasi, tes_kualifikasi

app_name = 'atlet'

urlpatterns = [
    path('daftar-sponsor/', daftar_sponsor, name='daftar_sponsor' ),
    path('form-kualifikasi/', form_tes_kualifikasi, name='form_tes_kualifikasi' ),
    path('tes-kualifikasi/', tes_kualifikasi, name='tes_kualifikasi' ),

]