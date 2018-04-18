from django.shortcuts import render
from django.http import HttpResponse
from .utils.utils import calculaMediaFinal

def index(request):

    return HttpResponse(calculaMediaFinal(8, 7))