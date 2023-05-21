from django.shortcuts import render
from Basdat_BaBaDu.helper.function import *
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
    context = {}
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO BABADU;")

    #GET DAFTAR EVENT
    query = sql_get_daftar_event()
    cursor.execute(query)
    data = parse(cursor)
    daftar_stadium = []
    for stadium in data:
        stadium['slug'] = title_to_slug(stadium['nama'])
        daftar_stadium.append(stadium)

    context['data_stadium'] = daftar_stadium

    return render(request, "daftar_event.html", context)


def detail_stadium(request, stadium):
    context = {}
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO BABADU;")

    #GET DETAIL STADIUM
    query = sql_get_detail_stadium(slug_to_title(stadium))
    cursor.execute(query)
    data = parse(cursor)
    daftar_event = []
    for event in data:
        event['total_hadiah'] = format_rupiah(event['total_hadiah'])
        event['slug'] = title_to_slug(event['nama_event'])
        daftar_event.append(event)

    context['daftar_event'] = daftar_event
    return render(request, "detail_stadium.html", context)

def detail_event(request, stadium, event):
    context = {}
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO BABADU;")

    #GET DETAIL EVENT
    query = sql_get_detail_event(slug_to_title(event))
    cursor.execute(query)
    data = parse(cursor)[0]

    for attribute in data:
        context[attribute] = data[attribute]
    context['total_hadiah'] = format_rupiah(context['total_hadiah'])

    #GET PARTAI KOMPETISI
    query = sql_get_partai_kompetisi(slug_to_title(event),context['tgl_mulai'].year )
    cursor.execute(query)
    data = parse(cursor)

    daftar_partai = []
    jenis_kelamin = 'Putra' if request.session['jenis_kelamin'] else 'Putri'
    for partai in data:
        if jenis_kelamin == 'Putra':
            if partai['jenis_partai'] == 'Ganda Putri' or partai['jenis_partai']  == 'Tunggal Putri':
                continue
        else:
            if partai['jenis_partai']  == 'Ganda Putra' or partai['jenis_partai']  == 'Tunggal Putra':
                continue
        daftar_partai.append(partai)
    context['jenis_partai'] = daftar_partai

    #GET PARTNER ATLET
    query = sql_get_partner(jenis_kelamin)
    cursor.execute(query)
    data = parse(cursor)
    return render(request, "detail_event.html", context)

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
        if context['status_kualifikasi'] == 'Qualified':
            request.session['is_qualified'] = True
        
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

