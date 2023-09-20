from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from main.forms import ProductForm
from main.models import Item


# Create your views here.
def show_main(request):
    all_products = Item.objects.all()

    context = {
        'application_name': 'Smart Inventory',
        'name': 'Fathirahma Alyssa Pristanti',
        'class': 'PBP F',
        'products': all_products,
        'item_count': all_products.count(),
    }

    return render(request, "inventory_main.html", context)

def create_new_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid and request.method == "POST":
        form.save()
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