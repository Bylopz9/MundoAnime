from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,"webapp/home.html")

def anime(request):
    return render(request,"webapp/anime.html")

def emision(request):
    return render(request,"webapp/emision.html")

def genero(request):
    return render(request,"webapp/genero.html")

def tienda(request):
    return render(request,"webapp/tienda.html")

def contacto(request):
    return render(request,"webapp/contacto.html")

def blog(request):
    return render(request,"webapp/blog.html")

def servicios(request):
    return render(request,"webapp/servicios.html")
