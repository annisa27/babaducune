from django.shortcuts import render

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