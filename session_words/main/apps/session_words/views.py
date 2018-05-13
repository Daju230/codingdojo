from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime

def index(request):
    if 'all_words' not in request.session:
        request.session['all_words'] = []
    return render(request, "index.html")



def add_word(request):
    if 'color' in request.POST:
        color = request.POST['color']
    else:
        color = "none"
    
    if 'big_font' in request.POST:
        big_font = "on"
    else:
        big_font = "off"
    
    request.session['all_words'].insert(0,{
        'word':request.POST['word'],
        'time': strftime("%H:%M%p %m on %x", gmtime()), 
        'color': color,
        'font': big_font
        })
    request.session.modified = True
    for i in request.session['all_words']:
        print len(i['word'])
    return redirect('/')

def clear(request):
    del request.session['all_words']
    print "++++CLEARED++++"
    return redirect('/')
