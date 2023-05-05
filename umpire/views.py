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