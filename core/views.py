from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenido al home de la aplicación Django.")