from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def plot(request):
    return render(request, "neutrons_U238.html")

def MathJax(request):
    return render(request, "MathJax.js")

def plotly_js(request):
    return render(request, "plotly-2.3.0.min.js")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
