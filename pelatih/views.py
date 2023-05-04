from django.shortcuts import render


# Create your views here.
def daftar_atlet(request):
    return render(request, "daftar_atlet.html")

def lihat_atlet(request):
    return render(request, "lihat_atlet.html")

def dashboard(request):
    return render(request, "dashboard.html")

# def show_register(request):
#     return render(request, "register.html")