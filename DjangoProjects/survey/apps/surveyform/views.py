from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'index.html')

def process(request):
	if 'submits' not in request.session:
		request.session['submits'] = 1
	else:
		request.session['submits'] += 1
		request.session['context'] = {
    	'name': request.POST['name'],
    	'location': request.POST['location'],
    	'language': request.POST['language'],
    	'comment': request.POST['textarea'],
    	}
	print "-" * 50
	return redirect('/results')

def results(request):
    print request.session['submits']
    context = request.session['context']
    return render(request, "results.html", context)

def back(request):
    return redirect('/')

def reset(request):
    print "=====SESSION CLEARED====="
    del request.session['submits']
    return redirect('/')


