from django.shortcuts import render


# Create your views here.
def list_event(request):
    return render(request, "list_event.html")

# def list_atlet(request):
#     return render(request, "list_atlet.html")

# def show_register(request):
#     return render(request, "register.html")

def dashboard(request):
    return render(request, "dashboard.html")