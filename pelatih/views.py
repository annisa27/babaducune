from django.shortcuts import render
from Basdat_BaBaDu.helper.function import parse
from django.shortcuts import render, redirect
from django.db import connection
from pelatih.query import *



# Create your views here.
def daftar_atlet(request):
    return render(request, "daftar_atlet.html")

def lihat_atlet(request):
    return render(request, "lihat_atlet.html")

def dashboard_pelatih(request):
    if "id" not in request.session:
        return redirect('authentication:login')
    
    context = {}
    if request.session['is_pelatih']:
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO BABADU;")

        #GET SPESIALISASI
        query = sql_get_spesialisasi(request.session['id'])
        cursor.execute(query)
        data = parse(cursor)

        daftar_spesialisasi = []
        for spesialisasi in data:
            daftar_spesialisasi.append(spesialisasi['spesialisasi'])
        daftar_spesialisasi = ', '.join(daftar_spesialisasi)
        context['spesialisasi'] = daftar_spesialisasi


    return render(request, "dashboard_pelatih.html", context)

# def show_register(request):
#     return render(request, "register.html")