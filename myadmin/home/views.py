from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse('this is a view which created by manish')
