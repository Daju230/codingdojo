from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, "index.html")

def add_to_cart(request):
    quantity = float(request.POST['quantity'])
   
    if request.POST['product_id'] == '1015':
        request.session['price'] = (19.99 * quantity)
    
    elif request.POST['product_id'] == '1016':
        request.session['price'] = (29.99 * quantity)
       

    elif request.POST['product_id'] == '1017':
        request.session['price'] = (4.99 * quantity)
       
    elif request.POST['product_id'] == '1018':
        request.session['price'] = (49.99 * quantity)
      
    if 'total' not in request.session:
        request.session['total'] = request.session['price']
    else:
        request.session['total'] += request.session['price']

    return redirect("/")

def checkout(request):
    return render(request, "checkout.html")

def clear(request):
    request.session['total'] =0
    return redirect("/")

def go_back(request):
    return redirect("/")