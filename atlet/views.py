from django.shortcuts import render
from Basdat_BaBaDu.helper.function import parse
from django.shortcuts import render, redirect
from django.db import connection
from atlet.query import *

# Create your views here.
def daftar_sponsor(request):
    return render(request, "daftar_sponsor.html")

def form_tes_kualifikasi(request):
    return render(request, "form_tes_kualifikasi.html")

def tes_kualifikasi(request):
    return render(request, "tes_kualifikasi.html")

def daftar_event(request):
    return render(request, "daftar_event.html")

def detail_stadium(request):
    return render(request, "detail_stadium.html")

def detail_event(request):
    return render(request, "detail_event.html")

def dashboard_atlet(request):
    if "id" not in request.session:
        return redirect('authentication:login')
    
    context = {}
    if request.session['is_atlet']:
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO BABADU;")

        #GET PELATIH
        query = sql_get_pelatih_atlet(request.session['id'])
        cursor.execute(query)
        data = parse(cursor)

        daftar_pelatih = []
        for pelatih in data:
            daftar_pelatih.append(pelatih['nama'])
        daftar_pelatih = ', '.join(daftar_pelatih)
        context['pelatih'] = daftar_pelatih
    
        #GET STATUS KUALIFIKASI
        query = sql_get_status_kualifikasi(request.session['id'])
        cursor.execute(query)
        data = parse(cursor)[0]

        for attribute in data:
            context[attribute] = data[attribute]
        
        #GET TOTAL POINT
        query = sql_get_total_point(request.session['id'])
        cursor.execute(query)
        data = parse(cursor)[0]
        context['total_point'] = data['total_point']

    return render(request, "dashboard_atlet.html", context)

def enrolled_event(request):
    return render(request, "enrolled_event.html")

def list_ujian_kualifikasi(request):
    return render(request, "list_ujian_kualifikasi.html")

