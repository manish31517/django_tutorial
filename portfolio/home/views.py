from django.shortcuts import render, HttpResponse
from home import models
# Create your views here.

def  home(request):
    context = {
        'name': 'harry',
        'course': 'Django'
    }
    return render(request, "home.html", context)
# def index(request):
#     return HttpResponse("This is my homepage ")
def about(request):
    # return HttpResponse("This is about")
    return render(request, "about.html")
def projects(request):
    # return HttpResponse("This is my project ")
    return render(request, "projects.html")
def contacts(request):
    if request.method == "POST" :
        print("This is post")
        name =request.POST['name']
        email= request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # print(name,email,phone,desc)
        ins = models.Contact(name=name,email=email,phone=phone,desc=desc)
        ins.save()
        print("The data has been written to the db")

    # return HttpResponse("This is contact")
    return render(request, "contact.html")