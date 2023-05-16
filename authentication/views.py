from django.shortcuts import render
import datetime
import uuid
from django.shortcuts import render, redirect
from django.db import connection, InternalError
from django.contrib import messages
from Basdat_BaBaDu.helper.function import parse
from authentication.query import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def show_home(request):
    request.session['nonauth'] = True
    return render(request, "home.html")


@csrf_exempt
def show_register(request):
    if request.method == 'POST':
        if 'submitAtlet' in request.POST:
            nama = request.POST.get('nama')
            email = request.POST.get('email')
            negara_asal = request.POST.get('negara_asal')
            tgl_lahir = request.POST.get('tgl_lahir')
            play_right = request.POST.get('play_right')
            height = request.POST.get('height')
            jenis_kelamin = request.POST.get('jenis_kelamin')
            data = register_atlet(nama, email, negara_asal, tgl_lahir, play_right, height, jenis_kelamin)
            if data['success']:
                return redirect('authentication:login')
            else:
                messages.info(request,data['msg'])
        elif 'submitPelatih' in request.POST:
            nama = request.POST.get('nama')
            email = request.POST.get('email')
            spesialisasi = request.POST.getlist('spesialisasi')
            tanggal_mulai = request.POST.get('tanggal_mulai')
            data = register_pelatih(nama, email, spesialisasi, tanggal_mulai)
            if data['success']:
                return redirect('authentication:login')
            else:
                messages.info(request,data['msg'])
        elif 'submitUmpire' in request.POST:
            nama = request.POST.get('nama')
            email = request.POST.get('email')
            negara = request.POST.get('negara')
            data = register_umpire(nama, email, negara)
            if data['success']:
                return redirect('authentication:login')
            else:
                messages.info(request,data['msg'])
    return render(request, 'register.html')

def register_atlet(nama, email, negara_asal, tgl_lahir, play_right, height, jenis_kelamin):
    try:
        id = uuid.uuid4()
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO BABADU;")
        query_member = sql_insert_member(id, nama, email)
        cursor.execute(query_member)
        query_atlet = sql_insert_atlet(id, tgl_lahir, negara_asal, play_right, height, jenis_kelamin)
        cursor.execute(query_atlet)
    except InternalError as e:
        return {
            'success': False,
            'msg': str(e.args)
        }
    else:
        return {
            'success': True,
        }
    
def register_pelatih(nama, email, spesialisasi, tanggal_mulai):
    try:
        id = uuid.uuid4()
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO BABADU;")
        query_member = sql_insert_member(id, nama, email)
        cursor.execute(query_member)
        query_pelatih = sql_insert_pelatih(id, tanggal_mulai)
        cursor.execute(query_pelatih)
        for i in spesialisasi:
            query_pelatih_spesialisasi = sql_insert_pelatih_spesialisasi(id, i)
            cursor.execute(query_pelatih_spesialisasi)
    except InternalError as e:
        return {
            'success': False,
            'msg': str(e.args)
        }
    else:
        return {
            'success': True,
        }

def register_umpire(nama, email, negara):
    try:
        id = uuid.uuid4()
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO BABADU;")
        query_member = sql_insert_member(id, nama, email)
        cursor.execute(query_member)
        query_umpire = sql_insert_umpire(id, negara)
        cursor.execute(query_umpire)
    except InternalError as e:
        return {
            'success': False,
            'msg': str(e.args)
        }
    else:
        return {
            'success': True,
        }

@csrf_exempt
def show_login(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        query_user = sql_get_user(nama, email)
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO BABADU;")
        cursor.execute(query_user) 
        data = parse(cursor)
        print(len(data))
        request.session['is_atlet'] = False
        request.session['is_pelatih'] = False
        request.session['is_umpire'] = False
        request.session['nonauth'] = False
        if len(data) == 1:
            member = data[0]
            print(member)
            for attribute in member:
                if isinstance(member[attribute], uuid.UUID):
                    request.session[attribute] = str(member[attribute])
                elif isinstance(member[attribute], datetime.date):
                    date = datetime.datetime.strptime(str(member[attribute]), '%Y-%m-%d')
                    formatted_date = date.strftime('%d %B %Y')
                    request.session[attribute] = formatted_date
                else:
                    request.session[attribute] = member[attribute]
            tipe = member['tipe_member']
            if tipe == 'atlet':
                request.session['is_atlet'] = True
                return redirect('atlet:dashboard_atlet')    
            elif tipe == 'pelatih':
                request.session['is_pelatih'] = True
                return redirect('pelatih:dashboard_pelatih') 
            elif tipe == 'umpire':
                request.session['is_umpire'] = True
                return redirect('umpire:dashboard_umpire')
            else:
                request.session['nonauth'] = True
        else:
            messages.info(request,'Username atau Password salah')

    return render(request, 'login.html')


def logout(request):
    request.session.clear()
    request.session['is_atlet'] = False
    request.session['is_pelatih'] = False
    request.session['is_umpire'] = False
    request.session['nonauth'] = True
    return redirect('authentication:home')

