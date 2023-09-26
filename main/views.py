import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from main.forms import ProductForm
from main.models import Item


# Restrict access to the main page only for logged in users
@login_required(login_url='/login')
# Create your views here.
def show_main(request):
    all_products = Item.objects.filter(user=request.user)

    for product in all_products:
        if(product.amount == 0):
            delete_product(request, product.id);
            return redirect('main:show_main')
 
    context = {
        'application_name': 'Smart Inventory',
        'name': request.user.username,
        'class': 'PBP F',
        'products': all_products,
        'item_count': len(all_products),
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "inventory_main.html", context)

def create_new_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, "create_new_product.html", context)


def show_xml(request):
    all_products = Item.objects.all()
    data = serializers.serialize('xml', all_products)
    return HttpResponse(data, content_type="application/xml")

def show_json(request):
    all_products = Item.objects.all()
    data = serializers.serialize('json', all_products)
    return HttpResponse(data, content_type="application/json")

def show_xml_by_id(request, id):
    product = Item.objects.filter(pk=id)
    data = serializers.serialize('xml', product)
    return HttpResponse(data, content_type="application/xml")

def show_json_by_id(request, id):
    product = Item.objects.filter(pk=id)
    data = serializers.serialize('json', product)
    return HttpResponse(data, content_type="application/json")

def register_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created successfully!')
            return redirect('main:show_main')
    else:
        form = UserCreationForm()
    return render(request, 'register_account.html', {'form': form})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, f'Username or password is incorrect! Please try again.')
    return render(request, 'login_user.html', {})

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def add_stock(request, product_id):
    product = get_object_or_404(Item, pk=product_id)
    product.amount += 1
    product.save()
    return redirect('main:show_main')

def reduce_stock(request, product_id):
    product = get_object_or_404(Item, pk=product_id)

    if product.amount > 0:
        product.amount -= 1
        product.save()
    return redirect('main:show_main')

def delete_product(request, product_id):
    product = get_object_or_404(Item, pk=product_id)
    product.delete()
    return redirect('main:show_main')