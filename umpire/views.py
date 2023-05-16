from django.shortcuts import render


# Create your views here.
def list_event(request):
    return render(request, "list_event.html")

# def list_atlet(request):
#     return render(request, "list_atlet.html")

# def show_register(request):
#     return render(request, "register.html")

def dashboard_umpire(request):
    return render(request, "dashboard_umpire.html")

def hasil_pertandingan(request):
    return render(request, "hasil_pertandingan.html")
def detail_hasil_pertandingan(request):
    return render(request, "detail_hasil_pertandingan.html")
def pertandingan(request):
    return render(request, "pertandingan.html")
def form_buat_ujian_kualifikasi(request):
    return render(request, "form_buat_ujian_kualifikasi.html")
def list_ujian_kualifikasi_umpire(request):
    return render(request, "list_ujian_kualifikasi_umpire.html")