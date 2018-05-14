from django.shortcuts import render, HttpResponse, redirect


def index(request):
    response = "placeholder to later display list of blogs"
    return render(request,"index.html")

def new(request):
    response = "plllaceholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    if request.method == "POST":
        return redirect('/')
    else:
        return redirect('/')

def show(request, number):
    response = "placeholder to display blog {}".format(number)
    return HttpResponse(response)

def edit(request, number):
    response = "placeholder to edit blog {}".format(number)
    return HttpResponse(response)

def destroy(request, number):
    return redirect('/')