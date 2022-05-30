from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# /products -> index

def index(request):
    return HttpResponse('Hello world')

def new(request):
    return HttpResponse('new products')

