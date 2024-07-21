
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Welcome to the index page!")

def about(request):
    return HttpResponse("This is the about page.")

def contact(request):
    return HttpResponse("Contact us at contact@example.com.")
