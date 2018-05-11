from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
	if 'attempts' not in request.session:
		request.session['attempts'] = 1
	else:
		request.session['attempts'] += 1

	random_word = get_random_string(length = 14, allowed_chars='abcdefghijklmnopqrstuvwxyz')
	content = {
		'random_word': random_word
	}
	print random_word

	print "====", request.session['attempts'], "===="
	
	return render(request, 'index.html', content)

def clear_session(request):
	if request.method == "POST":
		print "In clear"
		del request.session['attempts']
		print "cleared"
	return redirect('/')

def create(request):
	return redirect('/')
