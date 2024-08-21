from django.shortcuts import render
from galeria.models import Fotografia
# from django.http import HttpResponse

def index(request):
    fotos = Fotografia.objects.all()
    return render(request, "index.html", {"fotos": fotos})
    # return HttpResponse("<h1>Hello World</h1>")