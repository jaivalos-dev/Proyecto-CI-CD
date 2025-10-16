from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenido esto es un cambio.")